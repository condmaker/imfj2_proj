import pygame
import time
from Ship import *
from vector2 import *

def main():

    #ola
    pygame.init()
    screen = pygame.display.set_mode( (300, 300) )

    center = vector2(150,150)
    aship = Ship(center, 8)

    deltaTime = 0
    lastTime = time.time()

    while(True):

        keypressed = pygame.key.get_pressed()
        

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        if(keypressed[pygame.K_w]):
            aship.move_ship(-0.5)
        
        if(keypressed[pygame.K_s]):
            aship.move_ship(0.5)




        screen.fill( (0,0,59) )

        #pygame.draw.polygon(screen, (200,200,0), [(150,100),(140,160),(160,160)])
        aship.render_ship(screen)
        aship.UpdateCurrentVelocity(deltaTime)

        pygame.display.flip()

        deltaTime = time.time() - lastTime
        lastTime = time.time()
        #Personagem
        #screen.flip()
    

main()