# Here's the idea for these tools:
# You should be able to create multiple nested maps using the coordinate system objects.
# For instance, to create a 2D world map having 100 different places, I would create
# a coordSystem([],10,10,1) called "worldMap." I call the empty array so that it is clear that I am not
# mapped to anything else, thus this is the highest-level map.

# I could then create regional and local maps, giving them the appropriate positions when I initialize them, which then could
# be tied to even finer detailed maps or locations. I could also simply start creating locations in the world map, or even mix the two, with some
# areas simply being locations and others being other coordinate systems.   

import array
import os
import sys

class location:
	farDesc="" #For Descriptions of locations from far away
	nearDesc="" #For descriptions of locations from close-up
	name=""
	items=[] #I am investigating this, but apparently you can't use the "append" function with items and characters when there is an array of locations, i.e. a coordSystem locationArray. Don't know why this is.
	characters=[]		
	isCoordSys=False

	def __init__(self):
		self.farDesc = ""
		self.nearDesc = ""
		self.name = ""
		self.items = []
		self.characters = []
		self.isCoordSys = False #save time so that we don't have to check for a matching coordSys for every single location

	def __init__(self, isCoordSys):
		self.farDesc = ""
		self.nearDesc = ""
		self.name = ""
		self.items = []
		self.characters = []
		self.isCoordSys = isCoordSys

class coordSystem:
	xMax=0
	yMax=0
	zMax=0
	locationArray=[]

	def getLocation(self,x,y,z):
		return self.locationArray[z][y][x]

	def __init__(self,xMax,yMax,zMax):
		self.xMax=xMax
		self.yMax=yMax
		self.zMax=zMax
		self.locationArray=[ [ [location() for x in xrange(xMax)] for x in xrange(yMax) ] for x in xrange(zMax) ]
		#The above line is weird, but I can't think of a better way to initialize an array of arrays

