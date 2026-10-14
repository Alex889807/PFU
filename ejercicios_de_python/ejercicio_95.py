class AnalizadorNumeros:
    def procesar(self):
        pares = 0
        impares = 0
        positivos = 0
        negativos = 0
        
        continuar = True
        while continuar == True:
            num = int(input("Ingrese un número (0 para terminar): "))
            
            if num == 0:
                continuar = False
            else:
                if num % 2 == 0:
                    pares = pares + 1
                else:
                    impares = impares + 1
                    
                if num > 0:
                    positivos = positivos + 1
                elif num < 0:
                    negativos = negativos + 1
                    
        print("Números Pares:", pares)
        print("Números Impares:", impares)
        print("Números Positivos:", positivos)
        print("Números Negativos:", negativos)

ejercicio95 = AnalizadorNumeros()
ejercicio95.procesar()