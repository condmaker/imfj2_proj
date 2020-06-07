import pygame
from Rigidbody2d import *
from vector2 import *

class Ship(Rigidbody2d):

    def __init__(self, center, scale):
        super().__init__(center)
        
        self.center = center
        self.scale = scale
        self.line = [(0,0),(0,0),(0,0)]

        self.normalVect = vector2(0,1)
        self.tangentVect = vector2(1,0)

        self.velocity = vector2(0,0)
        self.acceleration = vector2(0,0)

 
    def render_ship(self, screen):
        self.construct_ship()
        pygame.draw.polygon(screen, (200,200,0) , self.line, 2)

    def construct_ship(self):
    
        self.center = self.get_center()

        self.line = [
            (self.center - (self.normalVect * self.scale * 2)).to_np2(),
            (self.center + (self.tangentVect * self.scale)).to_np2(),
            (self.center - (self.tangentVect * self.scale)).to_np2()
        ]

    def move_ship(self, moveVect):
        self.AddForce(self.normalVect * moveVect)
    
