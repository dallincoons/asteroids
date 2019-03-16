import arcade
from point import Point
from velocity import Velocity
import math
from flying_object import FlyingObject
from laser import Laser
from config import *

class Ship(FlyingObject):
    def __init__(self):
        super().__init__()

        self.center = Point(250, 250)
        self.alive = True
        self.velocity = Velocity(0, 0)
        self.angle = 0
        self.hit = 0
        self.gameOver = False
        self. speed = 0

        self.load_image()
        self.laser_sound = arcade.sound.load_sound("sounds/laser.wav")
        self.explosion_sound = arcade.sound.load_sound("sounds/explosion.wav")

    def load_image(self):
        if self.hit == 0:
            img = "images/playerShip1_orange.png"
        elif self.hit == 1:
            img = "images/damaged-ship.png"
        elif self.hit == 2:
            img = "images/damaged-ship.png"
        elif self.hit == 3:
            img = "images/explosion.png"

        self.texture = arcade.load_texture(img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        self.load_image()
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, alpha=1)

    def rotateLeft(self):
        if (self.angle > 360):
            self.angle = 0
        self.angle += SHIP_TURN_AMOUNT

    def rotateRight(self):
        if (self.angle < -360):
            self.angle = 0
        self.angle -= SHIP_TURN_AMOUNT

    def accelarate(self):
        if  self.speed < SHIP_MAX_THRUST:
            self.speed += SHIP_THRUST_AMOUNT

        self.velocity.dx = math.cos(math.radians(self.angle + 90)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle + 90)) * self.speed


    def decelerate(self):
        self.velocity.dx = 0
        self.velocity.dy = 0

    def fire(self, game):
        laser = Laser(self)
        game.lasers.append(laser)
        arcade.play_sound(self.laser_sound)

    def die(self):
        if not self.alive:
            self.draw()
            arcade.play_sound(self.explosion_sound)
            self.velocity = Velocity(0, 0)

    def handle_collision(self):
        self.hit +=1
        if self.hit >= 3:
            self.alive = False


