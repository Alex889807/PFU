class TablaMultiplicar:
    def iniciar(self):
        repetir = True
        while repetir == True:
            num = int(input("Ingrese el número para ver su tabla: "))
            
            print("--- Tabla del", num, "---")
            for i in range(1, 11):
                print(num, "x", i, "=", num * i)
                
            opcion = input("¿Desea ver la tabla de otro número? (S/N): ")
            opcion = opcion.upper()
            if opcion == "N":
                repetir = False

ejercicio90 = TablaMultiplicar()
ejercicio90.iniciar()