from flying_object import FlyingObject
import arcade
from point import Point
from velocity import Velocity
import math

class Laser(FlyingObject):
    def __init__(self, ship):
        super().__init__()
        self.center = Point(ship.center.x, ship.center.y)
        self.alive = True
        self.velocity = Velocity(math.cos(math.radians(ship.angle + 90)) * 10, math.sin(math.radians(ship.angle + 90)) * 10)
        self.angle = ship.angle + 90

        img = "images/laserBlue01.png"
        self.texture = arcade.load_texture(img)

        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, alpha=1)

    def advance(self):
        super().advance()
        if self.frames >= 60:
            self.die()
