class Ave:
    energiaMax = 0
    energia = 0
    especie = ''
    nombre = ''
    canto = ''

    def __init__(self,energiaMax,especie,nombre,canto):
        self.energiaMax = energiaMax
        self.energia = energiaMax
        self.especie = especie
        self.canto = canto
        self.nombre = nombre

    def get_energia(self):
        return self.energiaMax

    def get_especie(self):
        return self.especie

    def get_canto(self):
        return self.canto

    def get_nombre(self):
        return self.canto

    def set_energia(self,energia):
        self.energia = energia
    
    def set_especie(self,especie):
        self.especie = especie

    def set_canto(self,canto):
        self.canto = canto

    def set_nombre(self,nombre):
        self.nombre = nombre

    def describir(self):
        print("este es",self.nombre,"es un",self.especie,"su energia actual es de",str(self.energia)+"/"+str(self.energiaMax))

    def cantar(self):
        if(self.energia >= 10):
            self.energia -= 10
            print(self.nombre+" dice: " + self.canto)
        elif(self.energia < 10):
            print(self.nombre + " no tiene suficiente energia para cantar")

    def comer(self,cantidad):
        if (self.energia + cantidad <= self.energiaMax):
            self.energia += cantidad
            print("ahora",self.nombre,"tiene", str(self.energia),"/",str(self.energiaMax),"de energia")
        elif (self.energia + cantidad >= self.energiaMax):
            print(self.nombre,"ha comido hasta llenarse, han sobrado", str((self.energia+cantidad)-self.energiaMax), "de comida en su plato")
            self.energia = self.energiaMax

amarillito = Ave(50,"Pollito", 'Amarillito','pio pio') 
pepito = Ave(150,"Loro", "Pepito","Hola")
print("\n")
amarillito.describir()
pepito.describir()
print("\n")
amarillito.cantar()
pepito.cantar()
print("\n")
amarillito.comer(500)
pepito.comer(5)
print("\n")
