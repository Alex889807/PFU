class RegistroEdades:
    def registrar(self):
        mayores = 0
        menores = 0
        
        continuar = True
        while continuar == True:
            edad = int(input("Ingrese edad (0 para terminar): "))
            
            if edad == 0:
                continuar = False
            else:
                if edad >= 18:
                    mayores = mayores + 1
                else:
                    menores = menores + 1
                    
        print("Cantidad de mayores de edad:", mayores)
        print("Cantidad de menores de edad:", menores)

ejercicio94 = RegistroEdades()
ejercicio94.registrar()