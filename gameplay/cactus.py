import pygame

CACTUS1_PATH = "./assets/img/cactuses/cactus1.png"
CACTUS2_PATH  = "./assets/img/cactuses/cactus2.png"
CACTUS3_PATH  = "./assets/img/cactuses/cactus3.png"
CACTUS4_PATH  = "./assets/img/cactuses/cactus4.png"

class Cactus(pygame.sprite.Sprite):
    def __init__(self, img_path: str, speed: int, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed

    def update(self) -> None:
        self.rect.x -= self.speed
        if(self.rect.right < 0):
            self.kill()