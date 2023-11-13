#Jogo.py

import pygame
import os

pygame.init()

display_y = 600
display_x = 1100
screen = pygame.display.set_mode((display_y, display_x))

working = [pygame.image.load(os.path.join("Assets/Dino","DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino","DinoRun2.png"))]
jump = [pygame.image.load(os.path.join("Assets/Dino","DinoJump.png"))]
duck = [pygame.image.load(os.path.join("Assets/Dino","DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino","DinoDuck2.png"))]

small_cactus = [pygame.image.load(os.path.join("Assets/Cactus","SmallCactus1.png")),
           pygame.image.load(os.path.join("Assets/Cactus","SmallCactus2.png")),
           pygame.image.load(os.path.join("Assets/Cactus","SmallCactus2.png"))]
large_cactus = [pygame.image.load(os.path.join("Assets/Cactus","LargeCactus1.png")),
           pygame.image.load(os.path.join("Assets/Cactus","LargeCactus2.png")),
           pygame.image.load(os.path.join("Assets/Cactus","LargeCactus2.png"))]

bird =[pygame.image.load(os.path.join("Assets/Bird","Bird1.png")),
           pygame.image.load(os.path.join("Assets/Bird","Bird2.png"))]

cloud = pygame.image.load(os.path.join("Assets/Other","Cloud.png"))

bg = pygame.image.load(os.path.join("Assets/Other","Track.png"))

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        
