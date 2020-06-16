import pygame
import time
from ship import *
from gravity_well import *
from vector2 import *

def main():

    # Initializes pygame
    pygame.init()

    # Sets a predefined screen resolution
    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    # Loads the background image
    bg = pygame.image.load("background.png")

    # Defines what will be the center of the ship
    center = vector2(res[0] / 2, res[1] / 2)

    # Instatiate all entities
    aship = ship(center, 8)
    dumbwell = gravity_well(vector2(300,360), 105, 10000)
    well_2 = gravity_well(vector2(1000,360), 170, 10000)
    well_3 = gravity_well(vector2(640, 200), 80, 10000)

    # Initialize delta time
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

        # Fills the screen
        screen.fill( (0,0,59) )
        # Draws the background
        screen.blit(bg, (0, 0))

        # Update Ship      
        aship.render_ship(screen)
        aship.update_current_velocity(deltaTime)
        aship.update_angular_velocity(deltaTime)

        # Update Gravity Wells
        dumbwell.check_if_in_radius(aship, screen)
        dumbwell.render_well(screen)

        well_2.check_if_in_radius(aship, screen)
        well_2.render_well(screen)

        well_3.check_if_in_radius(aship, screen)
        well_3.render_well(screen)

        # Flips the display
        pygame.display.flip()

        # Updates the deltaTime
        deltaTime = time.time() - lastTime
        lastTime = time.time()

main()