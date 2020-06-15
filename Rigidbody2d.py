import pygame
from vector2 import *

class rigidbody2d:

    def __init__(self, center):
        self.center = center
        self.previousPos = center
        self.mass = 200 #kg

        self.acceleration = vector2(0,0)
        self.angularAcceleration = vector2(0,0)

        self.prevVelocity = vector2(0,0)
        self.currentVelocity = vector2(0,0)

        self.allForcesVect = []
        self.totalForce = vector2(0,0)
        self.inertiaMoment = 2
        pass

    def add_force(self, moveVect):
        self.allForcesVect.append(moveVect / self.mass)  #a = F/m
        pass

    # Torque - Vector2 to where the object will rotate to
    def add_torque(self, torque):
        self.angularAcceleration = torque / self.inertiaMoment

    def update_current_velocity(self, deltaTime):

        totalAcceleration = vector2(0,0)


        #Add all forces together 
        for force in self.allForcesVect:
            totalAcceleration += force
            self.allForcesVect.remove(force)

        self.acceleration = totalAcceleration


        self.previousPos = self.center

        self.currentVelocity = self.prevVelocity + (self.acceleration * deltaTime)
        print(self.currentVelocity)
        self.prevVelocity = self.currentVelocity

        self.center = self.previousPos + self.currentVelocity * deltaTime # <- Change this to position eq.
        self.acceleration = vector2(0,0)


    def update_angular_velocity(self):
        pass


    def get_center(self):
        return self.center