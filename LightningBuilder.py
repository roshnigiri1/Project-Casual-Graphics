from graphics import *
from math import *
from random import *
from playsound import playsound
import threading

class LightningBuilder:

    def __init__(self):
        randrange

    def drawLightningBranch(self, win):
        # loop needed for animation speed (can be sped up or slowed down)
        for i in range(1):
            def recursiveBoltBranch(line_center, recursion_dept):

                width = 3


                if recursion_dept == 5:
                    return False

                line = Line(Point(line_center.getX() + randrange(-5, 5), line_center.getY() + randrange(-5, 5)),
                            line_center)
                line.setOutline("yellow")
                line.setWidth(width)
                line.draw(win)

                line_center = line.getCenter()

                def deeperBoltRecursion(line_center, recursion_dept):
                    width = 1

                    if recursion_dept == 5:
                        return False

                    line = Line(Point(line_center.getX() + randrange(0,10), line_center.getY() + randrange(-10, 0)),
                                line_center)
                    line.setOutline("yellow")
                    line.setWidth(width)
                    line.draw(win)

                    line_center = line.getCenter()

                    deeperBoltRecursion(line_center, recursion_dept + 1)

                deeperBoltRecursion(line_center, 0)

                recursiveBoltBranch(line_center, recursion_dept + 1)

            def recursiveBolt(line_center, recursion_dept):

                width = 5

                if recursion_dept == 5:
                    return False

                nextPoint = Point(line_center.getX() + randrange(0, 20), line_center.getY() + randrange(-20, 0))

                line = Line(line_center, nextPoint)
                line.setOutline("yellow")
                line.setWidth(width)
                line.draw(win)
                line_center = line.getCenter()
                recursiveBoltBranch(line_center, 0)

                recursiveBolt(nextPoint, recursion_dept + 1)

            p1 = win.getMouse()
            soundName = "lightning.mp3"
            soundThread = threading.Thread(target=playsound, args=(soundName,))
            soundThread.start()

            recursiveBolt(p1, 0)

    def drawLightningFractal(self, win):
        def lightning(x, y, x2, y2):
            size = hypot(x - x2, y - y2)
            if size > 1:
                r = uniform(-0.2, 0.2)
                x1 = x + (x2 - x) / 2 - r * (y2 - y)
                y1 = y + (y2 - y) / 2 + r * (x2 - x)
                line = Line(Point(x, y), Point(x2, y2))

                lightning(x, y, x1, y1)
                lightning(x1, y1, x2, y2)
            else:
                line = Line(Point(x, y), Point(x2, y2))
                line.setOutline("yellow")
                line.setWidth(2)
                line.draw(win)

        for i in range(3):
            p3 = Point(randint(0, 100), randint(90, 100))
            p2 = win.getMouse()
            lightning(p3.getX(), p3.getY(), p2.getX(), p2.getY())
            soundName = "lightning.mp3"
            soundThread = threading.Thread(target=playsound, args=(soundName,))
            soundThread.start()

