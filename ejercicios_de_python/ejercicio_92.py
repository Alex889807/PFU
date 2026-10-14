class CalculadorAreas:
    def ejecutar(self):
        repetir = True
        while repetir == True:
            print("--- MENÚ DE ÁREAS ---")
            print("1. Cuadrado")
            print("2. Triángulo")
            print("3. Círculo")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "4":
                print("Programa terminado.")
                repetir = False
            elif opcion == "1":
                lado = float(input("Ingrese el lado del cuadrado: "))
                print("Área del Cuadrado:", lado * lado)
            elif opcion == "2":
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                print("Área del Triángulo:", (base * altura) / 2)
            elif opcion == "3":
                radio = float(input("Ingrese el radio del círculo: "))
                print("Área del Círculo:", 3.1416 * radio * radio) 
            else:
                print("Opción inválida.")

ejercicio92 = CalculadorAreas()
ejercicio92.ejecutar()