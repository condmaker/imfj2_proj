from vector2 import *
from Rigidbody2d import *
import pygame

class GravityWell():

    
    def __init__(self, center, range, force):
        
        self.center = center
        self.range = range
        self.force = force


    def check_if_in_radius(self, entity, screen):
        
        pos = entity.center

        if(pos == self.center):
            return


        if ( (pos.x - self.center.x) * (pos.x - self.center.x) + (pos.y - self.center.y) * (pos.y - self.center.y) < (self.range * self.range)   ):

            pygame.draw.line(screen, (250, 0, 0) , entity.center.to_np2() , self.center.to_np2())

            pullForce = self.center - entity.center
            pullForce.normalize()
            pullForce *= self.force
            #print(pullForce)
            entity.add_force(pullForce)


    def render_well(self, screen):

        pygame.draw.circle(screen, (0,250,170), self.center.to_np2(), self.range, 1)
