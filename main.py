class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

    def buscar(self, codigo_buscado):
        actual = self.cabeza

        while actual is not None:
            if actual.codigo == codigo_buscado:
                return actual
            actual = actual.siguiente

        return None

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

equipos = [
    ("PC01", "Equipo 1"),
    ("PC02", "Equipo 2"),
    ("PC03", "Equipo 3"),
]

lista = ListaEnlazada()
pila = Pila()
cola = Cola()

for codigo, descripcion in equipos:
    lista.agregar(codigo, descripcion)
    pila.apilar((codigo, descripcion))
    cola.encolar((codigo, descripcion))


print("=== Lista enlazada ===")
lista.mostrar()


print("\n=== Prueba de pila (LIFO) ===")
while True:
    elemento = pila.desapilar()

    if elemento is None:
        print("La pila está vacía.")
        break

    print("Retirado:", elemento)


print("\n=== Prueba de cola (FIFO) ===")
while True:
    elemento = cola.desencolar()

    if elemento is None:
        print("La cola está vacía.")
        break

    print("Atendido:", elemento)


print("\n=== Reto individual: buscar un código ===")
codigo_buscado = "PC02"
resultado = lista.buscar(codigo_buscado)

if resultado is not None:
    print(
        "Código encontrado:",
        resultado.codigo,
        "-",
        resultado.descripcion
    )
else:
    print("No se encontró el código:", codigo_buscado)


print("\n=== Prueba de código inexistente ===")
resultado = lista.buscar("PC99")

if resultado is None:
    print("No se encontró el código PC99.")
else:
    print(
        "Código encontrado:",
        resultado.codigo,
        "-",
        resultado.descripcion
    )