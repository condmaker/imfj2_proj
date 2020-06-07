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

        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        screen.fill( (0,0,59) )

        #pygame.draw.polygon(screen, (200,200,0), [(150,100),(140,160),(160,160)])
        aship.render_ship(screen)

        pygame.display.flip()

        deltaTime = time.time() - lastTime
        lastTime = time.time()
        #Personagem
        #screen.flip()
    

main()