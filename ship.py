import pygame
from Rigidbody2d import *
from vector2 import *

class ship(rigidbody2d):

    def __init__(self, center, scale):
        super().__init__(center)
        
        self.center = center
        self.scale = scale
        self.line = [vector2(0,0),vector2(0,0),vector2(0,0)]

        self.normalVect = vector2(0,1)
        self.tangentVect = vector2(1,0)

        self.velocity = vector2(0,0)
        self.acceleration = vector2(0,0)

 
    def render_ship(self, screen):

        self.construct_ship()
        
        newLines = []

        # Rotates all the lines accordingly (need to figure out the angles)
        for point in self.line:

            anotherVertice = vector2.from_np(point) - self.center
            finalVertice = vector2(0, 0)
            finalVertice.x = anotherVertice.x * math.cos(self.currentRotation) - anotherVertice.y * math.sin(self.currentRotation)
            finalVertice.y = anotherVertice.y * math.cos(self.currentRotation) + anotherVertice.x * math.sin(self.currentRotation)

            self.normalVect.x = -math.sin(self.currentRotation)
            self.normalVect.y = math.cos(self.currentRotation)
            point = (finalVertice + self.center).to_np2()
            newLines.append(point)

        self.line = newLines

        

        pygame.draw.polygon(screen, (200,200,0) , self.line, 2)

    def construct_ship(self):

        self.center = self.get_center()

        normVect = vector2(0,1)
        tanVect = vector2(1,0)

        
        newVect = vector2(0, 3)

        self.line = [
            (self.center - (normVect * self.scale * 3)).to_np2(),
            (self.center + (newVect + tanVect * self.scale)).to_np2(),
            (self.center - (-newVect + tanVect * self.scale)).to_np2()
        ]   

    def move_ship(self, moveVect):
        self.add_force(self.normalVect * moveVect)


    def rotate_ship(self, rotateVect, deltaTime):
        # Updates the angular velocity
        self.add_torque(rotateVect)
    
