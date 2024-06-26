import pygame
import sys
from objects.characters.Ability import Ability #Para obtener las habilidades
from objects.characters.character import Character #Para obtener al personaje
from assets.sprites.CharacterSprite import LoadedSprites
from assets.sprites.CharacterSprite import CharacterSprite #Para obtener personajes cargados

pygame.init()

#Configuración de la ventana
WIDTH, HEIGHT = 720, 500
WINDOWS_SIZE = (WIDTH, HEIGHT)
WIN = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption("Set War")
WHITE = (255,255,255)
BLACK = (0,0,0)
loads = LoadedSprites()

#Creación de habilidades
Corte = Ability(name="Corte",type="damage", power=30, energy_cost=10, health_cost=0)
Curar = Ability(name="Curar", type="heal", power=0,energy_cost=20, health_cost=0 )
Revivir = Ability(name="Revivir", type="heal", power=0, energy_cost=20, health_cost=70)

#Creación de personajes
Soldado = Character(name="Soldado", power=10, energy=20, health=100, abilities=[Corte])
Clerigo = Character(name="Clerigo", power=1, energy=20, health=70, abilities=[Curar, Revivir])


#Para cuando queramos usar una habilidad
# player.use_ability("Corte", enemy)
# player.use_ability("Heal", player_)

#Impresión de personajes

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 30)
        self.texts = ["Cantidad de caballeros", "Cantidad de arqueros", "Cantidad de clerigos:"]
        self.inputs = [0,0,0]
        self.start_button_rect = pygame.Rect(600,500,150,50)
        self.start_button_text = self.font.render("Iniciar Juego", True, BLACK)
    
    def draw(self):
        for i, text in enumerate(self.texts):
            text_surface = self.font.render(text, True, BLACK)
            WIN.blit(text_surface, (50, 50 + i * 50))
            pygame.draw.rect(WIN, BLACK, (350, 50 + i * 50, 50, 30))
            text_input = self.font.render(str(self.inputs[i]), True, BLACK)
            WIN.blit(text_input, (355, 55 + i * 50))
            
        pygame.draw.rect(WIN, BLACK, self.start_button_rect)
        WIN.blit(self.start_button_text, (self.start_button_rect.x + 20, self.start_button_rect.y + 15))
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(3):
                rect = pygame.Rect(350, 50 + i * 50, 50, 30)
                if rect.collidepoint(event.pos):
                    self.inputs[i] += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.start_button_rect.collidepoint(event.pos):
                return True
        return False    
        

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        WIN.fill(WHITE) 
        rey_sprite = CharacterSprite(loads.Rey1_sprite, 100, 100)
        rey_sprite.draw(WIN)
        pygame.display.update()
        
    pygame.quit()
    sys.exit()
    
    
if __name__ == "__main__":
    main()