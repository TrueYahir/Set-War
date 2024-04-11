import pygame

class CharacterSprite:
    def __init__(self, image_path, x, y):
        print("Camino",image_path)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        
class LoadedSprites:
    def __init__(self):
        self.Rey1_sprite = pygame.image.load("assets/sprites/rey1.png")
        self.Rey2_sprite = pygame.image.load("assets/sprites/rey2.png")
        self.caballero_sprite = pygame.image.load("assets/sprites/caballero.png")
        self.arquero_sprite = pygame.image.load("assets/sprites/arquero.png")
        self.clerigo_sprite = pygame.image.load("assets/sprites/clerigo.png")