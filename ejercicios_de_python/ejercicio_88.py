class SumaPromedio:
    def calcular(self):
        suma = 0
        n = int(input("¿Cuántos números desea ingresar?: "))
        
        for i in range(n):
            num = float(input("Ingrese un número: "))
            suma = suma + num
            
        promedio = suma / n
        print("Suma total:", suma)
        print("Promedio calculado:", promedio)

ejercicio88 = SumaPromedio()
ejercicio88.calcular()