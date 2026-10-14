class Calculadora:
    def mostrar_menu(self):
        repetir = True
        while repetir == True:
            print("--- MENÚ CALCULADORA ---")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "5":
                print("Calculadora finalizada.")
                repetir = False
            elif opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
                n1 = float(input("Ingrese primer número: "))
                n2 = float(input("Ingrese segundo número: "))
                
                if opcion == "1":
                    print("Resultado Suma:", n1 + n2)
                elif opcion == "2":
                    print("Resultado Resta:", n1 - n2)
                elif opcion == "3":
                    print("Resultado Multiplicación:", n1 * n2)
                elif opcion == "4":
                    if n2 != 0:
                        print("Resultado División:", n1 / n2)
                    else:
                        print("Error: No se puede dividir entre cero.")
            else:
                print("Opción inválida.")

ejercicio91 = Calculadora()
ejercicio91.mostrar_menu()