class MenuMultiuso:
    def lanzar_programa(self):
        repetir = True
        while repetir == True:
            print("--- MENÚ MATEMÁTICO ---")
            print("1. Calcular Factorial")
            print("2. Mostrar Tabla de Multiplicar")
            print("3. Comprobar Paridad")
            print("4. Calcular el Cuadrado")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "5":
                print("Saliendo...")
                repetir = False
            elif opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
                num = int(input("Ingrese el número para operar: "))
                
                if opcion == "1":
                    if num >= 0:
                        fact = 1
                        for i in range(1, num + 1):
                            fact = fact * i
                        print("El factorial es:", fact)
                    else:
                        print("No hay factorial de negativos.")
                elif opcion == "2":
                    for i in range(1, 11):
                        print(num, "x", i, "=", num * i)
                elif opcion == "3":
                    if num % 2 == 0:
                        print("Es un número PAR.")
                    else:
                        print("Es un número IMPAR.")
                elif opcion == "4":
                    print("El cuadrado es:", num * num)
            else:
                print("Opción incorrecta.")

ejercicio100 = MenuMultiuso()
ejercicio100.lanzar_programa()