import pygame
import math

PTERODACTYL1_PATH = "./assets/img/pterodactyls/pterodactyl1.png"
PTERODACTYL2_PATH = "./assets/img/pterodactyls/pterodactyl2.png"

class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, speed: int, x: int, y: int) -> None:
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load(PTERODACTYL1_PATH).convert_alpha())
        self.frames.append(pygame.image.load(PTERODACTYL2_PATH).convert_alpha())

        self.masks = []
        for frame in self.frames:
            self.masks.append(pygame.mask.from_surface(frame))
        
        self.image = self.frames[0]
        self.mask = self.masks[0]
        self.rect = self.image.get_rect(midbottom=(x, y))
        
        self.curr_frame = 0
        self.speed = speed

    def animation(self) -> None:
        self.curr_frame += 0.05
        if(self.curr_frame >= 2):
            self.curr_frame = 0
        self.image = self.frames[math.floor(self.curr_frame)]
        self.mask = self.masks[math.floor(self.curr_frame)]

    def update(self) -> None:
        self.animation()
        self.rect.x -= self.speed
        if(self.rect.right < 0):
            self.kill()
        
