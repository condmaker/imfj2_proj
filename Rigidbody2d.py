import pygame
from vector2 import *

class Rigidbody2d:

    def __init__(self, center):
        self.center = center
        self.acceleration = vector2(0,0)
        self.prevVelocity = vector2(0,0)
        self.currentVelocity = vector2(0,0)
        self.totalForce = vector2(0,0)
        pass

    def AddForce(self, moveVect):
        self.acceleration = moveVect
        pass

    def UpdateCurrentVelocity(self, deltaTime):
        self.currentVelocity = self.prevVelocity + (self.acceleration * deltaTime)
        self.prevVelocity = self.currentVelocity
        self.center += self.currentVelocity
        self.acceleration = vector2(0,0)


    def get_center(self):
        return self.center