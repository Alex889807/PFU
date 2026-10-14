class ContadorParesImpares:
    def procesar(self):
        pares = 0
        impares = 0
        
        for i in range(10):
            num = int(input("Ingrese un número entero: "))
            if num % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
                
        print("Cantidad de números pares:", pares)
        print("Cantidad de números impares:", impares)

ejercicio86 = ContadorParesImpares()
ejercicio86.procesar()