class CarritoCompras:
    def ingresar_productos(self):
        total = 0
        continuar = True
        
        while continuar == True:
            producto = input("Ingrese nombre del producto (o 'Finalizar' para terminar): ")
            producto = producto.upper()
            
            if producto == "FINALIZAR":
                continuar = False
            else:
                precio = float(input("Ingrese el precio: "))
                total = total + precio
                
        print("Compra terminada. Total a pagar:", total)

ejercicio96 = CarritoCompras()
ejercicio96.ingresar_productos()