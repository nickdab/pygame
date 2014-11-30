# These are some tools I am creating to help me build the map for the game. They are a work in progress.
# I am also learning python, so I apologize in advance if I do dumb things.

# Right now this consists of just two classes: locations and coordinate systems.
# As I have it implemented here, a coordinate system is simply a group of locations. 
# I'm sure there is more I could do, for instance linking a coordinate system to a location so that
# you could, for example, enter a house (a location on a larger map) and get a coordinate system
# for more detailed movement inside the house. Right now this is very possible to do,
# but it has to be implemented outside of the class.    

import array
import os
import sys


class location:
    farDesc = ""  # For Descriptions of locations from far away
    nearDesc = ""  # For descriptions of locations from close-up
    name = ""
    items = []  # I am investigating this, but apparently you can't use the "append" function with items and characters
                # when there is an array of locations, i.e. a coordSystem locationArray. Don't know why this is.
    characters = []
    isCoordSys = False

    def __init__(self):
        self.farDesc = ""
        self.nearDesc = ""
        self.name = ""
        self.items = []
        self.characters = []
        self.isCoordSys = False  # save time so that we don't have to check for a matching coordSys for every
                                 # single location


class coordSystem:
    name = ""
    xMax = 0
    yMax = 0
    zMax = 0
    _locationArray = []     # I have it as a "private variable" (as far as they exist in Python) to avoid confusion:
                            # as the implementation stands, you have to access the array in the order of [z][y][x], but
                            # most people are used to the opposite ordering. Rather than screw around with naming and
                            # perhaps add confusion, I want people to only ever access the array by get and set methods.

    def getLocation(self, x, y, z):
        return self._locationArray[z][y][x]

    def __init__(self, name, xMax, yMax, zMax):
        self.name = name
        self.xMax = xMax
        self.yMax = yMax
        self.zMax = zMax
        self._locationArray = [[[location() for x in range(xMax)] for x in range(yMax)] for x in range(zMax)]

    #The above line is weird, but I can't think of a better way to initialize an array of arrays