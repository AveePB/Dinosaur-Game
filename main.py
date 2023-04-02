from gameplay.pterodactyl import Pterodactyl
from gameplay.player import Player
from gameplay.ground import Ground
from gameplay.cloud import Cloud
from gameplay.cactus import *

import pygame 
import random
import math

SPAWN_OBSTACLE_TIME = 650
SPAWN_CLOUD_TIME = 800

ICON_PATH = "./assets/img/dino/dino1.png"
FONT_PATH = "./assets/font/press-start-2p.ttf"
FONT_COLOR = (83, 83, 83)
FONT_SIZE = 13
MAX_FPS = 60

HEIGHT = 210
WIDTH = 700
SPEED = 6

GAME_OVER_PATH = "./assets/img/game-over.png"
GAME_OVER = False

#creates the window
pygame.init()
main_surf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load(ICON_PATH))
pygame.display.set_caption("Dinosaur Game")
clock = pygame.time.Clock()

#SCORE/FONT
font = pygame.font.Font(FONT_PATH, FONT_SIZE)
score_diff = 0

#GAME OVER
game_over_surf = pygame.image.load(GAME_OVER_PATH)
game_over_rect = game_over_surf.get_rect(center=(math.floor(WIDTH/2), math.floor(HEIGHT/2)))

#EVENTS
SPAWN_CLOUD = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_CLOUD, SPAWN_CLOUD_TIME)

SPAWN_OBSTACLE = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_OBSTACLE, SPAWN_OBSTACLE_TIME)

#GROUND
ground1 = pygame.sprite.GroupSingle(Ground(SPEED, WIDTH-5, 0, HEIGHT-20))
ground2 = pygame.sprite.GroupSingle(Ground(SPEED, WIDTH-5, WIDTH,HEIGHT-20))

#CLOUDS
clouds = pygame.sprite.Group()

#OBSTACLES
obstacles = pygame.sprite.Group()

#PLAYER
player = pygame.sprite.GroupSingle(Player(100, HEIGHT-10))

while (True):
    #checks the current events
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        elif(event.type == SPAWN_CLOUD and not(GAME_OVER)):
            y = random.randint(1, 11) * 7
            clouds.add(Cloud(SPEED, WIDTH, y))
        elif(event.type == SPAWN_OBSTACLE and not(GAME_OVER)):
            obj_type = random.randint(0, 134) % 5
            if(obj_type == 0):
                obstacles.add(Pterodactyl(SPEED, WIDTH, HEIGHT-(random.randint(1, 5)*20)))
            else:
                cactus_type = random.randint(1, 134) % 4
                if(cactus_type == 1):
                    obstacles.add(Cactus(CACTUS1_PATH, SPEED, WIDTH, HEIGHT-14))
                elif(cactus_type == 2):
                    obstacles.add(Cactus(CACTUS2_PATH, SPEED, WIDTH, HEIGHT-10))
                elif(cactus_type == 3):
                    obstacles.add(Cactus(CACTUS3_PATH, SPEED, WIDTH, HEIGHT-12))
                else:
                    obstacles.add(Cactus(CACTUS4_PATH, SPEED, WIDTH, HEIGHT-15))
        elif(event.type == pygame.KEYDOWN and GAME_OVER):
            if(event.key == pygame.K_SPACE):
                score_diff = pygame.time.get_ticks()
                obstacles = pygame.sprite.Group()
                GAME_OVER = False
                
    if(GAME_OVER):
        continue

    #BACKGROUND
    main_surf.fill("white")

    #GROUND
    ground1.update()
    ground1.draw(main_surf)
    
    ground2.update()    
    ground2.draw(main_surf)
    
    #CLOUDS
    clouds.update()
    clouds.draw(main_surf)
    
    #SCORE
    curr_score = math.floor((pygame.time.get_ticks() - score_diff) / 90)
    score_surf = font.render(str(curr_score), False, FONT_COLOR)
    score_rect = score_surf.get_rect(topright=(WIDTH-10, 10))
    main_surf.blit(score_surf, score_rect)

    #OBSTACLES
    obstacles.update()
    obstacles.draw(main_surf)

    #PLAYER
    player.update()
    player.draw(main_surf)

    #detects the collision
    if(pygame.sprite.spritecollide(player.sprite, obstacles, False)):
        if(pygame.sprite.spritecollide(player.sprite, obstacles, False, pygame.sprite.collide_mask)):
            main_surf.blit(game_over_surf, game_over_rect)
            GAME_OVER = True
            
    pygame.display.update()
    clock.tick(MAX_FPS)