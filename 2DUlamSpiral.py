#
# This program creates a circular 2D Ulam spiral comprised of rings around one another.
# These rings are constructed by a series of segments. These segments are created as follows:

# An inner arc of a circle is traced using a specified angle, this is called the inner circle
# A normal line of length 1 is traced 'out' from the end of the arc
# From this line another arc (of the same angle as before) is traced backwards (this arc is called the outer circle)
# Finally, another normal line is traced, this one negative or 'in' so that the two arcs are connected.

# The first ring has an inner radius 1.5 and an outer radius of 2.5; it contains four segments which represent
#   the numbers 1-4, counting in a counter-clockwise fashion starting from -π/2 Rad (the bottom right segment)
# The next ring, placed around the first, has a inner radius of 2.5, and an outer radius of 3.5. This ring has 6
#   segments. where 5 is the first number counting counter-clockwise starting from -π/2 Rad (the bottom right segment)
# Each subsequent ring has an inner radius equal to the outer radius of the ring it encircles, and an
#  outer radius = inner radius + 1. In addition, each ring contains 2 more segments than the ring it encircles.

# The ideal circle size and number of segments is not arbitrary, each of the segments contains π area.
# Observe the following definition:
# r:d(x,y) = s
# r = ring number, where 1 is the inner most ring, 2 is the ring that encircles 1, etc...
# d(x,y) = |y^2 - x^2| = s = number of segments
# 1: d(1.5, 2.5) = 4
# 2: d(2.5, 3.5) = 6
# 3: d(3.5, 4.5) = 8 ...
#

import turtle
import math

numberOfRings = 30 #number of rings to be created
idealCircleSize = 1.5 #Set at 1.5 so that each segment has π area
scaleFactor = 15 #scale up for larger visual
resolution = 10 #number of points used to create arc of ring
turtle.pensize(2) #increase to increase thickness of lines
turtle.speed(0) #make 0 for instant creation,  5 for normal speed
radiusInnerCircle = idealCircleSize * scaleFactor
radiusOuterCircle = (idealCircleSize + 1) * scaleFactor
originInnerCircle = (0, 0)
pi = math.pi

turtle.setup(width = 1920, height = 1080, startx =None, starty = None)  # Pixel changes for screen size
#Checks numbers for primality
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
    return True


#
# The spiral is created using the following algorithm:
# 1: Determine number of rings to create
# 2: Determine number of segments to create in each ring
# 4: If Segment is prime, fill with color. Else, no color
# 5: Create segments (for more details, see line 5)


for ring in range(1, numberOfRings + 1):
    numberOfSegments = ring*2 + 2  # polynomial to calculate the number of segments per ring, interpolated (1. 4), (2, 6), (3, 8)...
    angleOfSegmentsDeg = 360 / numberOfSegments
    angleOfSegmentsRad = math.radians(angleOfSegmentsDeg)
    for segment in range(1, numberOfSegments + 1):
        xpos = math.cos(segment * angleOfSegmentsRad - (pi / 2)) * radiusOuterCircle
        ypos = math.sin(segment * angleOfSegmentsRad - (pi / 2)) * radiusOuterCircle + idealCircleSize * scaleFactor
        originOuterCircle = (xpos, ypos)
        if isPrime(segment + ring * ring + ring - 2):  # This formula determines the starting value for each ring
            turtle.up()
            turtle.setposition(originInnerCircle)
            turtle.down()
            turtle.fillcolor("gray")  # Change the color of primes here
            turtle.begin_fill()
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)
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
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)
            newOriginInnerCircle = turtle.position()
            turtle.setposition(originOuterCircle)
            turtle.circle(radiusOuterCircle, -angleOfSegmentsDeg, resolution)
            turtle.setposition(originInnerCircle)
            turtle.circle(radiusInnerCircle, angleOfSegmentsDeg, resolution)
            originInnerCircle = newOriginInnerCircle
    radiusInnerCircle = radiusOuterCircle
    radiusOuterCircle = radiusOuterCircle + scaleFactor
    originInnerCircle = (0, -scaleFactor * ring)
turtle.done()