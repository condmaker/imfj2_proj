import pygame
from vector2 import *

class Ship:

    def __init__(self, center, scale):
        self.center = center
        self.scale = scale
        self.normalVect = vector2(0,1)
        self.tangentVect = vector2(1,0)
 
    def render_ship(self, screen):
        self.construct_ship()
        pygame.draw.polygon(screen, (200,200,0) , self.polygon, 2)

    def construct_ship(self):
        self.polygon = [
            (self.center - (self.normalVect * self.scale * 2)).to_np2(),
            (self.center + (self.tangentVect * self.scale)).to_np2(),
            (self.center - (self.tangentVect * self.scale)).to_np2()
        ]

    