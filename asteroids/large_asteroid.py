from asteroids.asteroid import Asteroid
from point import Point
from velocity import Velocity
import random
from asteroids.medium_asteroid import MediumAsteroid
from asteroids.small_asteroid import SmallAsteroid
from config import *

class LargeAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.center = Point(500,300)
        self.velocity = Velocity(random.choice([-BIG_ROCK_SPEED, BIG_ROCK_SPEED]), random.choice([-BIG_ROCK_SPEED, BIG_ROCK_SPEED]))
        self.angle = 10
        self.alive = True
        self.radius = 15

    def get_image(self):
        return "images/meteorGrey_big1.png"

    def rotate(self):
        if self.angle == 360:
            self.angle = 0
        else:
            self.angle = self.angle + BIG_ROCK_SPIN

    def break_apart(self, game):
        if not self.alive:
            game.asteroids.append(MediumAsteroid.withStartingPoint(Point(self.center.x, self.center.y + 2)))
            game.asteroids.append(MediumAsteroid.withStartingPoint(Point(self.center.x, self.center.y - 2)))
            game.asteroids.append(SmallAsteroid.withStartingPoint(Point(self.center.x + 5, self.center.y )))
