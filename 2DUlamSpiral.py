import turtle
import math

numberOfCircles = 19 #how many complete circles to create
idealCircleSize = 1 #use 1 for starting 3 sections, use 1.5 for starting 4 sections
scaleFactor = 17 #scale up for better visual
radiusInnerCircle = idealCircleSize * scaleFactor
radiusOuterCircle = (idealCircleSize + 1) * scaleFactor
originInnerCircle = (0, 0)
pi = math.pi

resolution = 10 #how many points used to create a circle with turtle
turtle.pensize(2) #increase to increase thickness oof lines
turtle.speed(0) #make 0 for instant creation,  5 for normal speed


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True #pri


for circles in range(1, numberOfCircles + 1):
    numberOfSegments = (circles - 1) * 2 + 4  # (circles-1)*2 + 3 for 3 section start,
    angleOfSegmentsRad = math.radians(360 / numberOfSegments)
    angleOfSegmentsDeg = 360 / numberOfSegments

    for segment in range(1, numberOfSegments + 1):
        xpos = math.cos(segment * angleOfSegmentsRad - (pi / 2)) * radiusOuterCircle
        ypos = math.sin(segment * angleOfSegmentsRad - (pi / 2)) * radiusOuterCircle + idealCircleSize * scaleFactor  # dont forget to correct for the offset
        originOuterCircle = (xpos, ypos)

        if isPrime(segment + circles * circles + circles - 2) == True:  # circles*circles - 1 for starting 3 sections
            turtle.up()
            turtle.setposition(originInnerCircle)
            turtle.down()
            turtle.fillcolor("gray")
            turtle.begin_fill()
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)  # turtle requires degrees to operate
            newOriginInnerCircle = turtle.position()
            turtle.setposition(originOuterCircle)
            turtle.circle(radiusOuterCircle, -angleOfSegmentsDeg, resolution)
            turtle.setposition(originInnerCircle)
            turtle.end_fill()
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)
            originInnerCircle = newOriginInnerCircle
        else:
            turtle.up()
            turtle.setposition(originInnerCircle)
            turtle.down()
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)  # turtle requires degrees to operate
            newOriginInnerCircle = turtle.position()
            turtle.setposition(originOuterCircle)
            turtle.circle(radiusOuterCircle, -angleOfSegmentsDeg, resolution)
            turtle.setposition(originInnerCircle)
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)
            originInnerCircle = newOriginInnerCircle

    radiusInnerCircle = radiusOuterCircle
    radiusOuterCircle = radiusOuterCircle + scaleFactor
    originInnerCircle = (0, -scaleFactor * circles)


turtle.done()
