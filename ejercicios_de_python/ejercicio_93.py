class RegistroNotas:
    def recopilar(self):
        suma = 0
        cantidad = 0
        mayor = 0
        menor = 0
        
        continuar = True
        print("Ingrese las notas. Use un número negativo para terminar.")
        
        while continuar == True:
            nota = float(input("Ingrese nota: "))
            
            if nota < 0:
                continuar = False
            else:
                suma = suma + nota
                cantidad = cantidad + 1
                
                if cantidad == 1:
                    mayor = nota
                    menor = nota
                else:
                    if nota > mayor:
                        mayor = nota
                    if nota < menor:
                        menor = nota
                        
        if cantidad > 0:
            promedio = suma / cantidad
            print("Promedio general:", promedio)
            print("Nota más alta:", mayor)
            print("Nota más baja:", menor)
        else:
            print("No se ingresaron notas.")

ejercicio93 = RegistroNotas()
ejercicio93.recopilar()