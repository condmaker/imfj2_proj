from vector2 import *
from rigidbody2d import *
import pygame

class gravity_well():

    def __init__(self, center, range, force):
        self.center = center
        self.range = range
        self.force = force

    # Observes if an object is inside the radius of a well.
    def check_if_in_radius(self, entity, screen):
        pos = entity.center

        if(pos == self.center):
            return

        if ( (pos.x - self.center.x) * (pos.x - self.center.x) + (pos.y - self.center.y) * (pos.y - self.center.y) < (self.range * self.range) ):

            pygame.draw.line(screen, (250, 0, 0), entity.center.to_np2(), self.center.to_np2())

            pullForce = self.center - entity.center
            pullForce.normalize()
            pullForce *= self.force
            #print(pullForce)
            entity.add_force(pullForce)

    # Renders the well.
    def render_well(self, screen):
        pygame.draw.circle(screen, (0,250,170), self.center.to_np2(), self.range, 1)
