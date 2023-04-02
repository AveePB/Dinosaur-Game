import pygame

GROUND_PATH  = "./assets/img/ground.png"

class Ground(pygame.sprite.Sprite):
    def __init__(self, speed: int, new_x: int, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(GROUND_PATH).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.new_x = new_x

    def update(self) -> None:
        self.rect.x -= self.speed
        if(self.rect.right < 0):
            self.rect.x = self.new_x