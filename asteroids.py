import pygame
from Ship import *

def main():

    #ola
    pygame.init()
    screen = pygame.display.set_mode( (300, 300) )
    aship = Ship(0,0)

    while(True):

        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        screen.fill( (0,0,59) )

        #pygame.draw.polygon(screen, (200,200,0), [(150,100),(140,160),(160,160)])
        aship.render_ship(screen)

        pygame.display.flip()

        #Personagem
        #screen.flip()
    

main()