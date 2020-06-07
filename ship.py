import pygame

class Ship:

    def __init__(self, center, scale):
        self.center = center
        self.scale = scale
        self.polygon = [(150,100),(140,160),(160,160)]
 
    def render_ship(self, screen):
        pygame.draw.polygon(screen, (200,200,0) , self.polygon)

    def construct_ship(self):
        pass