class Vehiculo:
    def __init__(self, marca, modelo, capacidad_combustible):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_combustible = capacidad_combustible
    
    def __str__(self):
        return "Maraca: " + self.marca + " Modelo: " + self.modelo
    
    def moverse(self):
        print("El vehículo de la marca ", self.marca, " modelo ", self.modelo, "está en movimiento.")

class MovmientosEmbarcacion:
    def virara_a_estribor(self):
        print("Esta embarcación está virando a estribor")   
    def virara_a_babor(self):
        print("Esta embarcación está virando a babor")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, comb, color, numero_de_puertas):
        super().__init__(marca, modelo, comb)
        self.color = color
        self.puertas = numero_de_puertas

    def tocar_bocina(self):
        print("El auto está haciendo piii piii")



class Lancha(Vehiculo, MovmientosEmbarcacion):
    def __init__(self, marca, modelo, comb, asientos, calado):
        super().__init__(marca, modelo, comb)
        self.asientos = asientos
        self.calado = calado

automovil_1 = Auto("Toyota", "Corolla", 50, "Verde", 5)
automovil_2 = Auto("Audi", "A4", 45, "Blanco", 3)

lancha_1 = Lancha("Yamaha", "125", 30, 5, 1.5)

print(automovil_1)
print(lancha_1)

automovil_1.moverse()
lancha_1.virara_a_babor()
lancha_1.virara_a_estribor()
automovil_1.tocar_bocina()
