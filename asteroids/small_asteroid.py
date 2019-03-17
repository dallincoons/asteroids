from asteroids.asteroid import Asteroid
from point import Point
from velocity import Velocity
import random
from config import *

class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.center = Point(200, 40)
        self.velocity = Velocity(random.choice([-1.5, 1.5]), random.choice([-1.5, 1.5]))
        self.angle = 10
        self.radius = 2

    def get_image(self):
        return "images/meteorGrey_small1.png"

    def rotate(self):
        if self.angle == 360:
            self.angle = 0
        else:
            self.angle = self.angle + SMALL_ROCK_SPIN

    def break_apart(self, game):
        self.alive = False
