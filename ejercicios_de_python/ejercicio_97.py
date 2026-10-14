class MenuBancario:
    def mostrar_cajero(self):
        saldo = 500.0
        repetir = True
        
        while repetir == True:
            print("\n--- CAJERO ELECTRÓNICO ---")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "4":
                print("Operación terminada.")
                repetir = False
            elif opcion == "1":
                print("Su saldo actual es:", saldo)
            elif opcion == "2":
                monto = float(input("Cantidad a depositar: "))
                if monto > 0:
                    saldo = saldo + monto
                    print("Depósito exitoso.")
                else:
                    print("Monto inválido.")
            elif opcion == "3":
                monto = float(input("Cantidad a retirar: "))
                if monto <= saldo:
                    saldo = saldo - monto
                    print("Retiro exitoso.")
                else:
                    print("Error: Fondos insuficientes.")
            else:
                print("Opción incorrecta.")

ejercicio97 = MenuBancario()
ejercicio97.mostrar_cajero()