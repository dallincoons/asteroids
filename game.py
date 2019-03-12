"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
from asteroids.large_asteroid import LargeAsteroid
from asteroids.medium_asteroid import MediumAsteroid
from asteroids.small_asteroid import SmallAsteroid
from point import Point
from ship import Ship
from config import *
from threading import Timer

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        self.asteroids = []

        self.lasers = []

        self.asteroids.append( LargeAsteroid.withStartingPoint(Point(50, 100)) )
        self.asteroids.append( LargeAsteroid.withStartingPoint(Point(50, SCREEN_HEIGHT - 200)) )
        self.asteroids.append( LargeAsteroid.withStartingPoint(Point(400, SCREEN_HEIGHT - 100)) )
        self.asteroids.append( LargeAsteroid.withStartingPoint(Point(SCREEN_WIDTH - 100, 400)) )
        self.asteroids.append( LargeAsteroid.withStartingPoint(Point(SCREEN_WIDTH - 100, 50)) )

        self.ship = Ship()

        self.game_over = False


        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        if self.game_over == True:
            arcade.draw_text("YOU LOSE :(", 100, 300, arcade.color.WHITE, 70)
            return


        for asteroid in self.asteroids:
            asteroid.draw()

        for laser in self.lasers:
            laser.draw()

        if self.ship.alive:
            self.ship.draw()
        else:
            self.ship.die()
            self.game_over = True

        self.win()

    def update(self, delta_time):
        """
        Update each object in the game.
        """
        self.check_keys()

        for asteroid in self.asteroids:
            asteroid.advance()

        for laser in self.lasers:
            laser.advance()

        self.ship.advance()
        self.check_collisions()
        self.cleanup()

    def check_collisions(self):
        for laser in self.lasers:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if laser.alive and asteroid.alive:
                    too_close = laser.radius + asteroid.radius

                    if (abs(laser.center.x - asteroid.center.x) < too_close and
                            abs(laser.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        laser.alive = False
                        asteroid.alive = False
                        asteroid.break_apart(self)

        # Now, check for anything that is dead, and remove it
        self.cleanup()

        for asteroid in self.asteroids:
            # Make sure they are both alive before checking for a collision
            if self.ship.alive and asteroid.alive:
                too_close = self.ship.radius + asteroid.radius

                if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                        abs(self.ship.center.y - asteroid.center.y) < too_close):
                    # its a hit!
                    self.ship.hit +=1
                    if self.ship.hit >= 3:
                        self.ship.alive = False
                    asteroid.alive = False
                    asteroid.break_apart(self)

        # Now, check for anything that is dead, and remove it
        self.cleanup()

    def cleanup(self):
        for laser in self.lasers:
            if not laser.alive:
                self.lasers.remove(laser)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def win(self):
        if len(self.asteroids) <= 0:
            arcade.draw_text("YOU WIN!!", 200, 300, arcade.color.WHITE, 70)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.rotateLeft()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotateRight()

        if arcade.key.UP in self.held_keys:
            self.ship.accelarate()

        if arcade.key.DOWN in self.held_keys:
            self.ship.decelerate()

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                self.ship.fire(self)
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
