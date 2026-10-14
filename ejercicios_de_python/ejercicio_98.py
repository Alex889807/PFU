class EstadisticasNotas:
    def procesar(self):
        aprobados = 0
        reprobados = 0
        
        for i in range(10):
            nota = float(input("Ingrese nota del alumno: "))
            
            if nota >= 51:
                aprobados = aprobados + 1
            else:
                reprobados = reprobados + 1
                
        print("Alumnos Aprobados:", aprobados)
        print("Alumnos Reprobados:", reprobados)

ejercicio98 = EstadisticasNotas()
ejercicio98.procesar()