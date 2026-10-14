class ClasificadorEdades:
    def evaluar(self):
        ninos = 0
        adolescentes = 0
        adultos = 0
        mayores = 0
        
        n = int(input("¿Cuántas edades va a registrar?: "))
        for i in range(n):
            edad = int(input("Ingrese edad: "))
            
            if edad <= 11:
                ninos = ninos + 1
            elif edad <= 17:
                adolescentes = adolescentes + 1
            elif edad <= 64:
                adultos = adultos + 1
            else:
                mayores = mayores + 1
                
        print("Niños:", ninos)
        print("Adolescentes:", adolescentes)
        print("Adultos:", adultos)
        print("Adultos Mayores:", mayores)

ejercicio99 = ClasificadorEdades()
ejercicio99.evaluar()