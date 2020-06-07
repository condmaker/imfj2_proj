import pygame
import time
from Ship import *

def main():

    #ola
    pygame.init()
    screen = pygame.display.set_mode( (300, 300) )
    aship = Ship(0,0)

    deltaTime = 0
    lastTime = time.time()

    while(True):

        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        screen.fill( (0,0,59) )

        #pygame.draw.polygon(screen, (200,200,0), [(150,100),(140,160),(160,160)])
        aship.RenderShip(screen)

        pygame.display.flip()

        deltaTime = time.time() - lastTime
        lastTime = time.time()
        #Personagem
        #screen.flip()
    

main()