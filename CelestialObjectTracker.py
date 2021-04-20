from graphics import *
from CelestialObject import CelestialObject

class CelestialObjectTracker:
    def __init__(self, win, angle, velocity, height, timeOfDay):
        """win is the GraphWin to display the shot . angle, velocity,
            and height are initial sun parameters .
        """
        #create an object representing the sun or the moon
        self.object = CelestialObject(angle, velocity, height)

        #if time of day is a string night chosen by the user create a marker representing the sun
        if timeOfDay == "Night":
            self.marker = Circle(Point(0, height), 10)
            self.marker.setFill("yellow")
            self.marker.setOutline("yellow")
            self.marker.draw(win)

        #if time of day is a string night chosen by the user create a marker representing the moon
        if timeOfDay == "Day":
            self.marker = Circle(Point(0, height), 8)
            self.marker.setFill("white")
            self.marker.setOutline("white")
            self.marker.draw(win)

    def update(self, dt):
        """Move the object dt seconds farther along its flight"""

        # update the object
        self.object.update(dt)

        # move the marker representing sun or moon to the new projectile location
        center_marker = self.marker.getCenter()
        dx = self.object.getX() - center_marker.getX()
        dy = self.object.getY() - center_marker.getY()
        self.marker.move(dx, dy)

    def getX(self):
        """return the current x coordinate of the object's center"""
        return self.object.getX()

    def getY(self):
        """return the current y coordinate of the object's center"""
        return self.object.getY()

    def setX(self):
        """return the current x coordinate of the object's center"""
        self.object.setX()

    def setY(self):
        """return the current y coordinate of the object's center"""
        self.object.setY()

    def undraw(self):
        """undraw the object"""
        self.marker.undraw()