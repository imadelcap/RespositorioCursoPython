class Auto():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
        # Con esto alcanza para definir la clase
    
    def __str__(self):
        return "Auto: " + self.marca + ", modelo: " + self.modelo
    

auto1 = Auto("BMW", "320")

print(auto1)