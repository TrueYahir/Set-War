from objects.characters.Ability import Ability
from objects.characters.character import Character

class Ejercito:
    def __init__(self, facciones):
        self.facciones = facciones
        
    def get_facciones(self):
        return self.facciones
    
    def set_facciones(self, faccion):
        self.facciones = faccion
        
    def informacion(self):
        #Imprimimos la cantidad de tropas
        pass
        
    def ataque(self, enemy_player, uso, ataque):
        for j in enemy_player.facciones[ataque - 1]:
            j.receive_damage(self.facciones[uso - 1][0].power)
            j.energy -= j.abilities.energy_cost
            
        for i in self.facciones[uso - 1]:
            i.receive_damage(enemy_player.facciones[ataque - 1][0].power)
            i.energy -= i.abilities.energy_cost
            
    def curar(self, curador, curados):
        for i in self.facciones[curador - 1]:
            i.energy -= i.abilities.enegy_cost
        for j in self.facciones[curados - 1]:
            if j.healtg > 0 and j.health <= 88:
                j.healt += self.facciones[curador - 1][0].abilities.power
                
    def remover(self):
        for i in self.facciones[0][:]:
            if i.health <= 0:
                self.facciones[0].remove(i)
        for j in self.facciones[1][:]:
            if j.health <= 0:
                self.facciones[1].remove(j)
        for k in self.facciones[2][:]:
            if k.health <= 0:
                self.facciones[0].remove(k)