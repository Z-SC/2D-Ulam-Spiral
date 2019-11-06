#
# Note that this program was created using CADQuery, and must be run
# with FreeCAD. If you do not have FreeCAD, Download it from the link below
# and use the link below that get CADQuery
# https://www.freecadweb.org/downloads.php
# https://github.com/jmwright/cadquery-freecad-module/blob/master/docs/installation.md
#

#primality test, returns true if prime
def isprime(n): 
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
# This program can only create a cube, where numCubes (the variable name in the program) 
# is the number of units in the X and Y and Z direction.
# the origin is at (1,1,1) the lattice is created first along the positive X-axis first, then along positive Y, then positive Z.
# mathematically, the following definition applies: (x,y,z) = n
# where x, y, z, n  are natural numbers, (x,y,z) is a location in 3-space, and n is the number we're counting.

# (1, numCubes, numCubes) = 1, 
# (2, numCubes, numCubes) = 2, 
# (3, numCubes, numCubes) = 3, ...

# (1, numCubes - 1, numCubes) = numCubes + 1, 
# (1, numCubes - 2, numCubes) = numCubes + numCubes + 1, 
# (1, numCubes - 3, numCubes) = numCubes + numCubes + numCubes + 1, ...

# (1, numCubes, numCubes - 1) = numCubes^2 + 1, 
# (1, numCubes, numCubes - 2) = 2*numCubes^2 + 1,
# (1, numCubes, numCubes - 3) = 3*numCubes^2 + 1, ...

# (numCubes, numCubes, numCubes) = numCubes
# (numCubes, 1, 1) = numCubes*numCubes*numCubes

import cadquery as cq
import math
planes = ["XY", "YZ", "XZ"]
quartets = ['Q1', 'Q2', 'Q3']
cubeSize = 4 #individual cube size
pilonDiameter = .1 #thickness of lines of the latice
numCubes = 5 #number of cubes in XYZ planes

# Begins the creation of the lattice, which is comprised of a (numCubes x numCubes x numCubes) matrix,
# this is visualized by gridlines of varying thickness.
# Another way to visualize this is a series of hollowed cubes, with all the faces removed and only the lines connecting the 
# vertices remaining. These lines are of varying thickness


numberOne = cq.Workplane("XY").box(cubeSize, cubeSize, cubeSize, centered =(False, False, False))
primes = numberOne
for i in range(3):
	xoffset = 2*i - i*i #polynomial that acts an on/off switch for the offsets
	yoffset = i*i/2 - 3*i/2 + 1 #polynomial that acts an on/off switch for the offsets
	quartets[i] = cq.Workplane(planes[i]).center(-cubeSize*xoffset, -cubeSize*yoffset)\
	.rect(cubeSize, cubeSize, centered=False, forConstruction=True).vertices().circle(pilonDiameter).extrude(cubeSize) 
#CadQuery allows the creation of objects on the corners of a rect(angle), this creates three sets of four circles, each four in a square shape in the three planes listed above. the circles are then extruded to create lines.

#create a singular unit cube from intersection of the thee sets of four lines
unitCube= quartets[0].union(quartets[1]).union(quartets[2]) 
cubeCols = unitCube
for x in range(numCubes-1):  # Create each 'column' along the positive X-axis; each column is one unit cube
	cubeColsX = cubeCols.translate((cubeSize,0,0))
	cubeCols =  cubeColsX.union(cubeCols)
	
unitRow = cubeCols  # Create each 'row' along the positive Y-axis; rows are comprised of (numCubes) unit cubes along the x axis
cubeRows = unitRow
for y in range(numCubes-1): 
	cubeRowsY = cubeRows.translate((0,cubeSize,0))
	cubeRows = cubeRowsY.union(cubeRows)

unitPlane = cubeRows
cubePlanes = unitPlane

for z in range(numCubes-1):  #finally we create each 'plane' along the positive Z-axis; planes are comprised of a (numCubes x numCubes) set of unit cubes
	cubePlanesZ = cubePlanes.translate((0, 0, cubeSize)) 
	cubePlanes = cubePlanesZ.union(cubePlanes)

# Here begins the creation of the solid cubes which represent prime numbers.
for number in range (2, numCubes*numCubes*numCubes+1):
	if isprime(number) == True:
		xoffset = number % numCubes - 1
		yoffset = math.floor(number / numCubes) % numCubes
		zoffset = math.floor(number/(numCubes*numCubes))
		if number == numCubes:
			xoffset = numCubes - 1
			yoffset = 0
			zoffset = 0
		prime = cq.Workplane("XY").box(cubeSize, cubeSize, cubeSize, centered =(False, False, False))\
		.translate((cubeSize*xoffset, -cubeSize*yoffset, -cubeSize*zoffset))
		primes = prime.union(primes)

#This offset is not working, currently I cant match up the skeleton to the cube set
#cubePlanes = cubePlanes.translate((0,-cubeSize/2,0))
primes = primes.translate((0,cubeSize*numCubes,cubeSize*numCubes))
show_object(primes, options={"rgba":(204, 204, 204, 0.0)})
show_object(cubePlanes, options={"rgba":(204, 204, 204, 0.0)})