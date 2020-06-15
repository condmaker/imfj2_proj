import pygame
import time
from ship import *
from GravityWells import *
from vector2 import *

def main():

    #ola
    pygame.init()

    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    center = vector2(res[0] / 2, res[1] / 2)

    #Instatiate Entities
    aship = ship(center, 8)
    dumbwell = GravityWell(vector2(300,360), 105, 10000)

    well_2 = GravityWell(vector2(1000,360), 170, 1000000)

    well_3 = GravityWell(vector2(640, 200), 80, 10000)

    deltaTime = 0
    lastTime = time.time()

    while(True):

        keypressed = pygame.key.get_pressed()
        

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        if(keypressed[pygame.K_w]):
            aship.move_ship(-5000) # Valor em Newton
        
        if(keypressed[pygame.K_s]):
            aship.move_ship(5000) # Valor em Newton

        if(keypressed[pygame.K_a]):
            aship.rotate_ship(-2, deltaTime) # Valor em Newton

        if(keypressed[pygame.K_d]):
            aship.rotate_ship(2, deltaTime) # Valor em Newton




        screen.fill( (0,0,59) )


        #Update Ship      
        aship.render_ship(screen)
        aship.update_current_velocity(deltaTime)
        aship.update_angular_velocity(deltaTime)

        #Update Wells
        dumbwell.check_if_in_radius(aship, screen)
        dumbwell.render_well(screen)

        well_2.check_if_in_radius(aship, screen)
        well_2.render_well(screen)

        well_3.check_if_in_radius(aship, screen)
        well_3.render_well(screen)



        pygame.display.flip()

        deltaTime = time.time() - lastTime
        lastTime = time.time()
        #Personagem
        #screen.flip()
    

main()