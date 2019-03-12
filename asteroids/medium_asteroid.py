from asteroids.asteroid import Asteroid
from asteroids.small_asteroid import SmallAsteroid
from point import Point
from velocity import Velocity
import random

class MediumAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.center = Point(50,50)
        self.velocity = Velocity(random.choice([-1.5, 1.5]), random.choice([-1.5, 1.5]))
        self.angle = 10
        self.radius = 5

    def get_image(self):
        return "images/meteorGrey_med1.png"

    def rotate(self):
        if self.angle == 360:
            self.angle = 0
        else:
            self.angle = self.angle - 2

    def break_apart(self, game):
        if not self.alive:
            game.asteroids.append(SmallAsteroid.withStartingPoint(Point(self.center.x + 1.5, self.center.y + 1.5)))
            game.asteroids.append(SmallAsteroid.withStartingPoint(Point(self.center.x - 1.5, self.center.y - 1.5)))
