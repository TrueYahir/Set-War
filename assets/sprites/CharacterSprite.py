import pygame

class CharacterSprite:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        
class LoadedSprites:
    def __init__(self):
        self.Rey1_sprite = pygame.image.load("sprites/rey1.png")
        self.Rey2_sprite = pygame.image.load("sprites/rey2.png")
        self.caballero_sprite = pygame.image.load("sprites/caballero.png")
        self.arquero_sprite = pygame.image.load("sprites/arquero.png")
        self.clerigo_sprite = pygame.image.load("sprites/clerigo.png")