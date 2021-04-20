from graphics import *
from ButtonLightning import Button

class InputDialog:
    """A custom window for getting simulation values (angle, velocity,
    and height) from the user."""

    def __init__(self, angle, vel, height):
        """Build and display the input window"""
        self.win = win = GraphWin("Initial Values", 200, 400)
        win.setCoords(0, 0, 12, 12)

        #changes the position of the input box
        x = 800
        y = 200
        win.master.geometry('%dx%d+%d+%d' % (200, 400, x, y))

        #create button that for summer action
        self.summer = Button(win, Point(6, 1), 12, 2, "Summer")
        self.summer.activate()
        #create button that for summer winter
        self.winter = Button(win, Point(6, 3), 12, 2, "Winter")
        self.winter.activate()
        #create button that for lightning action
        self.lightning_branch = Button(win, Point(6, 5), 12, 2, "Lightning Branch")
        self.lightning_branch.activate()
        # create button that for lightning action
        self.lightning_fractal = Button(win, Point(6, 7), 12, 2, "Lightning Fractal")
        self.lightning_fractal.activate()
        #create button that for night action
        self.night = Button(win, Point(6, 9), 12, 2, "Night")
        self.night.activate()
        #create button that for day action
        self.day = Button(win, Point(6, 11), 12, 2, "Day")
        self.day.activate()

    def interact(self):
        """ wait for user to click button
        Returns a string indicating which button was clicked"""
        while True:
            pt = self.win.getMouse()
            if self.summer.clicked(pt):
                return "Summer"
            if self.winter.clicked(pt):
                return "Winter"
            if self.lightning_branch.clicked(pt):
                return "Lightning Branch"
            if self.lightning_fractal.clicked(pt):
                return "Lightning Fractal"
            if self.night.clicked(pt):
                return "Night"
            if self.day.clicked(pt):
                return "Day"

    def close(self):
        """close the input window"""
        self.win.close()

    def activateDay(self):
        self.day.activate()

    def activateNight(self):
        self.night.activate()

    def deactivateDay(self):
        self.day.deactivate()

    def deactivateNight(self):
        self.night.deactivate()