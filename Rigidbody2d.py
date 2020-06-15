import pygame
from vector2 import *

class rigidbody2d:

    def __init__(self, center):
        self.center = center
        self.previousPos = center
        self.mass = 200 #kg

        self.acceleration = vector2(0,0)
        self.angularAcceleration = 0

        self.prevVelocity = vector2(0,0)
        self.currentVelocity = vector2(0,0)

        self.prevAngVelocity = 0
        self.currentAngVelocity = 0

        self.prevRotation = 0
        self.currentRotation = 0

        self.allForcesVect = []
        self.currentRotation = 0
        self.totalForce = vector2(0,0)
        self.inertiaMoment = 2
        pass

    def add_force(self, moveVect):
        self.allForcesVect.append(moveVect / self.mass)  #a = F/m
        pass

    # Torque - Vector2 to where the object will rotate to, torque given in Newton
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

        # Velocity cap so that the ship doesn't fly away
        if (self.currentVelocity.y >= 0.5):
            self.currentVelocity.y = 0.5
        elif (self.currentVelocity.y <= -0.5):
            self.currentVelocity.y = -0.5
        if (self.currentVelocity.x >= 0.5):
            self.currentVelocity.x = 0.5
        elif (self.currentVelocity.x <= -0.5):
            self.currentVelocity.x = -0.5

        print(self.currentVelocity)

        self.prevVelocity = self.currentVelocity
<<<<<<< HEAD

        self.center = self.previousPos + self.currentVelocity * deltaTime # <- Change this to position eq.
=======
        self.center += self.currentVelocity # <- Change this to position eq.

>>>>>>> marco_branch
        self.acceleration = vector2(0,0)


    def update_angular_velocity(self, deltaTime):
        # Updates the current and old angular velocity
        self.currentAngVelocity = self.prevAngVelocity + (self.angularAcceleration * deltaTime)

        # Calculates the angle that the object will turn
        self.currentRotation = self.prevRotation + self.prevAngVelocity * deltaTime + (self.angularAcceleration * (deltaTime * deltaTime)) / 2

        # Updates the old angular velocity with the new one
        self.prevAngVelocity = self.currentAngVelocity
        self.prevRotation = self.currentRotation
        self.angularAcceleration = 0

    def get_center(self):
        return self.center