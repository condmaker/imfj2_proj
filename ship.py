import pygame
from Rigidbody2d import *

class Ship(Rigidbody2d):

    def __init__(self, center, scale):
        super().__init__()
        self.center = center
        self.scale = scale
        self.lines = [(150,100),(140,160),(160,160)]
 
    def RenderShip(self, screen):
        pygame.draw.lines(screen, (200,200,0), True, self.lines)

    def ConstructShip(self):
        pass