import pygame
import math

DEFAULT_DINO_PATH = "./assets/img/dino/dino1.png"
DINO2_PATH = "./assets/img/dino/dino2.png"
DINO3_PATH = "./assets/img/dino/dino3.png"
DINO4_PATH = "./assets/img/dino/dino4.png" 
DINO5_PATH = "./assets/img/dino/dino5.png" 

JUMP = -13
class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load(DEFAULT_DINO_PATH).convert_alpha())
        self.frames.append(pygame.image.load(DINO2_PATH).convert_alpha())
        self.frames.append(pygame.image.load(DINO3_PATH).convert_alpha())
        self.frames.append(pygame.image.load(DINO4_PATH).convert_alpha())
        self.frames.append(pygame.image.load(DINO5_PATH).convert_alpha())

        self.masks = []
        for frame in self.frames:
            self.masks.append(pygame.mask.from_surface(frame))
        
        self.image = self.frames[0]
        self.mask = self.masks[0]
        self.rect = self.image.get_rect(midbottom=(x, y))

        self.curr_frame = 0
        self.gravity = 0
        self.floor = y
    
    def player_input(self) -> None:
        keyboard = pygame.key.get_pressed()
        if(keyboard[pygame.K_UP] and self.rect.bottom >= self.floor):
            self.image = self.frames[0]
            self.mask = self.masks[0]            
            self.gravity = JUMP
        elif(keyboard[pygame.K_DOWN] and self.rect.bottom == self.floor):
            self.curr_frame = max(self.curr_frame, 3)
            self.curr_frame += 0.1
            
            if(self.curr_frame > 5):
                self.curr_frame = 3

            self.image = self.frames[math.floor(self.curr_frame)]
            self.mask = self.masks[math.floor(self.curr_frame)]

    def animation(self) -> None:
        keyboard = pygame.key.get_pressed()
        if(keyboard[pygame.K_DOWN] and self.rect.bottom == self.floor):
            return
        if(self.floor != self.rect.bottom):
            return
        
        self.curr_frame = max(self.curr_frame, 1)
        self.curr_frame += 0.1

        if(self.curr_frame > 3):
            self.curr_frame = 1
        
        self.image = self.frames[math.floor(self.curr_frame)]
        self.mask = self.masks[math.floor(self.curr_frame)]

    
    def apply_gravity(self) -> None:
        self.gravity += 1
        self.rect.y += self.gravity
        if(self.rect.bottom >= self.floor):
            self.rect.bottom = self.floor

    def update(self) -> None:
        self.animation()
        self.player_input()
        self.apply_gravity()

