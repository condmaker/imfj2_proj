import pygame
from vector2 import *

class rigidbody2d:

    def __init__(self, center):
        self.center = center
        self.previousPos = center
        self.mass = 200 

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

    # Adds a force to the object
    def add_force(self, moveVect):
        self.allForcesVect.append(moveVect / self.mass)  

    # Torque - Vector2 to where the object will rotate to, in Newton.
    def add_torque(self, torque):
        self.angularAcceleration = torque / self.inertiaMoment

    # Updates the current velocity of the instanced object.
    def update_current_velocity(self, deltaTime):
        # Initializes the 'totalAcceleration' variable as a vector2
        totalAcceleration = vector2(0,0)

        # Add all forces together 
        for force in self.allForcesVect:
            totalAcceleration += force
            self.allForcesVect.remove(force)

        # Equalizes the current acceleration to the total acceleration with 
        # all forces in consideration
        self.acceleration = totalAcceleration
        # Sets the previous position as the center
        self.previousPos = self.center
        # Updates current velocity
        self.currentVelocity = self.prevVelocity + (self.acceleration * deltaTime)
        # Sets previous velocity equal to the current one in order to make 
        # other updates possible
        self.prevVelocity = self.currentVelocity
        # Utilizes the position equation to calculate the updated position
        self.center = self.previousPos + self.currentVelocity * deltaTime 
        
        # Resets the acceleration
        self.acceleration = vector2(0,0)


    # Updates the angular velocity of the instanced object.
    def update_angular_velocity(self, deltaTime):
        # Updates the current and old angular velocity
        self.currentAngVelocity = self.prevAngVelocity + (self.angularAcceleration * deltaTime)

        # Calculates the angle that the object will turn
        self.currentRotation = self.prevRotation + self.prevAngVelocity * deltaTime + (self.angularAcceleration * (deltaTime * deltaTime)) / 2

        # Updates the old angular velocity with the new one
        self.prevAngVelocity = self.currentAngVelocity
        self.prevRotation = self.currentRotation
        self.angularAcceleration = 0

    # Gets the center of the object.
    def get_center(self):
        return self.center