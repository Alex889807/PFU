class Validador:
    def solicitar_opcion(self):
        continuar = True
        while continuar == True:
            respuesta = input("¿Desea continuar? (S/N): ")
            respuesta = respuesta.upper() 
            
            if respuesta == "S" or respuesta == "N":
                print("Opción válida registrada:", respuesta)
                continuar = False # Rompe el ciclo
            else:
                print("Opción inválida. Intente de nuevo.")

ejercicio85 = Validador()
ejercicio85.solicitar_opcion()