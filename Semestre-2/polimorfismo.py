class Vehiculo:
    def avanzar(self):
        print("El vehículo avanza")

class Auto(Vehiculo):
    def avanzar(self):
        print("El auto está conduciendo")

class Bicicleta(Vehiculo):
    def avanzar(self):
        print("La bicicleta está pedaleando")

def mover_vehiculo(v):
    v.avanzar()

mover_vehiculo(Auto())
mover_vehiculo(Bicicleta())
