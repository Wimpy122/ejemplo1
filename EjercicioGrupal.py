from datetime import datetime, timedelta, date

class BikeUnavailableError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class InvalidReservationError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


 
class Bike:
    def __init__(self, Modelo):
        self.modelo = Modelo
        self.estado = "Disponible"

    def cambiar_estado(self):
        try:
            if self.estado == "Disponible":
                self.estado = "Ocupado"               

            elif self.estado == "Ocupado":
                self.estado = "Disponible"
                      
        except Exception as e:
            print(f"Error: {e}")
        
        finally:    
            print(f"la Bici {self.modelo} ahora esta {self.estado}!")
        
        

class Reservation:
    def __init__(self, bici, cliente, inicio, fin):
        try:
            
            
            self.bike = bici
            self.cliente = cliente
            self.inicio = inicio
            self.fin = fin
            self.duracion = (fin - inicio).days
            tarifa_por_dia = 240
            self.precio = tarifa_por_dia * self.duracion
            self.estado = "Activa"

            if bici.estado != "Disponible":
                self.estado = "Fallida"
                raise BikeUnavailableError("Esta Bici ya esta ocupada.")           
        
            if self.inicio > self.fin:
                self.estado = "Fallida"
                raise InvalidReservationError("Fecha de reservacion no valida.")
            
            
            self.bike.cambiar_estado() 

        except Exception as e:
                print(f"Error: {e}")
            
        finally:
                print(f"Intento Completado")                
                print(f"Reservacion {self.estado}")

    def finalizar(self):
        self.estado = "completada"
        self.bike.cambiar_estado()
        print(f"${self.precio}")


#    a. Crear una bicicleta nueva e imprimirla.
bici1 = Bike("BMX")
print(vars(bici1))
bici2 = Bike("Urbana")
print(vars(bici2))

#    b. Crear una reserva válida dentro de un bloque try/except/finally:
#         - Atrapar BikeUnavailableError e InvalidReservationError y mostrar el error.
#         - En finally, imprimir que se intentó la reserva.
reserva1 = Reservation(bici1, "gabriel", date.fromisoformat('2025-08-05'), date.fromisoformat('2025-08-07'))

print(vars(reserva1))
print(vars(bici1))

#    c. Intentar reservar la misma bicicleta de nuevo (debe fallar con BikeUnavailableError).
reserva2 = Reservation(bici1, "pepe", date.fromisoformat('2025-08-05'), date.fromisoformat('2025-08-08'))

#    d. Intentar crear una reserva con fechas inválidas (fin antes de inicio) para provocar InvalidReservationError.

reserva3 = Reservation(bici2, "Juan", date.fromisoformat('2025-08-05'), date.fromisoformat('2025-08-02'))

#    e. Finalizar la reserva original y mostrar que la bicicleta vuelve a estar disponible.
reserva1.finalizar()
print(vars(bici1))

#    f. Crear otra reserva ahora que la bicicleta está libre y mostrarla.

reserva4 = Reservation(bici1, "Javier", date.fromisoformat('2025-08-08'), date.fromisoformat('2025-08-10'))
print(vars(reserva4))

# 7. Al final, imprimir el estado final de la bicicleta y de la(s) reserva(s) para verificar lo sucedido.

print(vars(reserva1))
print(vars(reserva2))
print(vars(reserva3))
print(vars(reserva4))
print(vars(bici1))
print(vars(bici2))
