import pygame
import time
from ship import *
from vector2 import *

def main():

    #ola
    pygame.init()

    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    center = vector2(res[0] / 2, res[1] / 2)
    aship = ship(center, 8)

    deltaTime = 0
    lastTime = time.time()

    while(True):

        keypressed = pygame.key.get_pressed()
        

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        if(keypressed[pygame.K_w]):
            aship.move_ship(-0.2) # Valor em Newton
        
        if(keypressed[pygame.K_s]):
            aship.move_ship(0.2) # Valor em Newton

        if(keypressed[pygame.K_a]):
            aship.rotate_ship(-2, deltaTime) # Valor em Newton

        if(keypressed[pygame.K_d]):
            aship.rotate_ship(2, deltaTime) # Valor em Newton




        screen.fill( (0,0,59) )

        #pygame.draw.polygon(screen, (200,200,0), [(150,100),(140,160),(160,160)])
        aship.render_ship(screen)
        aship.update_current_velocity(deltaTime)

        pygame.display.flip()

        deltaTime = time.time() - lastTime
        lastTime = time.time()
        #Personagem
        #screen.flip()
    

main()