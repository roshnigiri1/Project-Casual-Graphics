from graphics import *
from CustomInputLightning import InputDialog
from BackgroundBuilder import BackgroundBuilder
from LightningBuilder import LightningBuilder
from CelestialObjectTracker import CelestialObjectTracker

# create a 500, 400 window
win = GraphWin("Lightning", 1200, 600, autoflush=False)

# set coordinates to go from (0 , 0) in the lower left
# to (100 , 100) in the upper right .
win.setCoords(0.0, 0.0, 100, 100)

#create background builder object
background = BackgroundBuilder(win)

#create lightning builder object
lightning = LightningBuilder()



def dialog():
    while True:
        # interact with the user
        inputwin = InputDialog(2, 2, 2)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Summer":
            background.changeSeason(win,"Summer")

        if choice == "Winter":
            background.changeSeason(win,"Winter")

        if choice == "Lightning Branch":
            lightning.drawLightningBranch(win)

        if choice == "Lightning Fractal":
            lightning.drawLightningFractal(win)

        if choice == "Night":
            background.duringTheChangingOfNight(win)
            objectAction("Night")
            background.changeTimeOfDay(win, "Night")

        if choice == "Day":
            background.duringTheChangingOfDay(win)
            objectAction("Day")
            background.changeTimeOfDay(win, "Day")


def objectAction(timeOfDay):

    # initial object for the celestial object
    objectTrack = CelestialObjectTracker(win, 30, 30, 80, timeOfDay)
    while 0 <= objectTrack.getY() <= 100 and -10 < objectTrack.getX() <= 110:
        objectTrack.update(1 / 50)
        update(50)


dialog()