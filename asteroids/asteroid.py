import arcade
import random
from point import Point
from velocity import Velocity
from abc import ABC, abstractmethod
from flying_object import FlyingObject

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Asteroid(FlyingObject):

    def __init__(self):
        super().__init__()
        self.center = Point(250, 250)
        self.angle = 0
        self.velocity = Velocity(0, 0)
        self.alive = True

        img = self.get_image()
        self.texture = arcade.load_texture(img)

        self.width = self.texture.width
        self.height = self.texture.height

    @classmethod
    def withStartingPoint(cls, point):
        asteroid =  cls()
        asteroid.center.x = point.x
        asteroid.center.y = point.y
        return asteroid

    @abstractmethod
    def get_image(self):
        pass

    def draw(self):
        alpha = 1

        x = self.center.x
        y = self.center.y
        self.rotate()

        arcade.draw_texture_rectangle(x, y, self.texture.width, self.texture.height, self.texture, self.angle, alpha)

    @abstractmethod
    def rotate(self):
        pass

    @abstractmethod
    def break_apart(self, game):
        pass
