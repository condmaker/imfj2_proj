import pygame
from vector2 import *

class Rigidbody2d:

    def __init__(self):
        self.acceleration = vector2(0,0)
        self.prevVelocity = vector2(0,0)
        self.currentVelocity = vector2(0,0)
        self.totalForce = vector2(0,0)
        pass

    def AddForce(self):
        pass

    def UpdateCurrentVelocity(self, deltaTime):
        self.currentVelocity = self.prevVelocity + (self.acceleration * deltaTime)
        self.prevVelocity = self.currentVelocity
