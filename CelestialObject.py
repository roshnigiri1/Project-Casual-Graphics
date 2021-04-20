from math import sin, cos, radians

class CelestialObject:
    """Simulates the flight of simple celestial object such as sun or moon near the earth's
    surface , ignoring wind resistance . Tracking is done in two
    dimensions , height (y) and distance (x) . """

    def __init__(self, angle, velocity, height):
        """Create a object with given launch angle , initial
        velocity and height . """
        self.xpos = 20
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this object to move it time seconds farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 10 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getX(self):
        "Returns the x position (distance) of this object ."
        return self.xpos

    def getY(self):
        "Returns the y position (height) of this object ."
        return self.ypos

    def setX(self):
        "Returns the x position (distance) of this object ."
        self.xpos = -9

    def setY(self):
        "Returns the y position (height) of this object ."
        self.ypos = 30