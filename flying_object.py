from velocity import Velocity
from point import Point
from abc import ABC, abstractmethod

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FlyingObject(ABC):
    def __init__(self):
        self.center = Point(500,300)
        self.velocity = Velocity(0, 0)
        self.frames = 0
        self.radius = 30

    def advance(self):
        self.center.x = self.center.x + self.velocity.dx
        self.center.y = self.center.y + self.velocity.dy

        self.frames += 1

        self.wrap()

    def die(self):
        self.alive = False


    def wrap(self):
        if self.center.y < -self.height:
            self.center.y = SCREEN_HEIGHT + self.height
        elif self.center.y > (SCREEN_HEIGHT + self.height):
            self.center.y = -self.height
        elif self.center.x < -self.width:
            self.center.x = SCREEN_WIDTH + self.width
        elif self.center.x > (SCREEN_WIDTH + self.width):
            self.center.x = -self.width
