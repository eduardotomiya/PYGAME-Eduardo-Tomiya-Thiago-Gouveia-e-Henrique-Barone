#Jogo.py

import pygame
import os

pygame.init()

display_y = 
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

#altura e largura do personagem
class Dinosaur:
    x_pos=80
    y_pos=310

    
    def init(self):
        self.duck_img=duck
        self.run_img=RUNNing
        self.jump_img=jump
        
def main():
    run = True
    clock = pygame.time.Clock()
    #completar com o personagem
    player= ()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((255,255,255))
        userInput=pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()
