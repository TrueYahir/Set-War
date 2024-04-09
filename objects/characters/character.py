#Esta clase es la clase base para los personajes

class Character:
    def __init__(self, name, health, power, energy, abilities):
        self.name = name
        self.health = health
        self.max_health = health
        self.power = power
        self.energy = energy
        self.abilities = abilities
        self.defense_duration = 0
        
    def attack(self, target):
        target.health -= self.power
    
    def receive_damage(self, damage):
        damage -= self.defense_duration
        if damage < 0:
            damage = 0
        self.health -= damage
    
    def defend(self, duration):
        self.defense_duration += duration
        #Verificar que se active la defensa
    
    def use_ability(self, ability_name, target):
        for ability in self.abilities:
            if ability.name == ability_name:
                if self.energy >= ability.energy_cost and self.health >= ability.healht_cost:
                    ability.use(target)
                    self.energy -= ability.energy_cost
                    self.health -= ability.healt_cost
                    break
                
    def end_turn(self):
        if self.defense_duration > 0:
            self.defense_duration -= 1