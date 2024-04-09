#Clase para el uso de habilidades
class Ability:
    def __init__(self, name,type, power, energy_cost, health_cost, defense_duration=0):
        self.name = name
        self.type = type
        self.power = power
        self.energy_cost = energy_cost
        self.healt_cost = health_cost
        self.defense_duration = defense_duration
        
    def use(self, character):
        if self.type == "damage":
            character.receive_damage(self.power)
        elif self.type == "heal":
            character.heal(self.power)
        elif self.type == "defense":
            character.defend(self.defense_duration)
        else:
            pass
            #Aquí vamos a poner algo en caso de haber un error