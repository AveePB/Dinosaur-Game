import pygame

CLOUD_PATH  = "./assets/img/cloud.png"

class Cloud(pygame.sprite.Sprite):
    def __init__(self, speed: int, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(CLOUD_PATH).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self) -> None:
        self.rect.x -= self.speed
        if(self.rect.right < 0):
            self.kill()