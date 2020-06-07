import pygame

def main():

    #ola
    pygame.init()
    screen = pygame.display.set_mode( (300, 300) )

    while(True):

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        screen.fill( (0,0,59) )
        pygame.display.flip()

        #Personagem
        #screen.flip()
    

main()