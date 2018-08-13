#!/usr/bin/env python

"""Map_Gen

Map generation and tools module.  Allows for the generation of procedurally created maps.
"""

__version__ = '0.16'
__author__ = 'Gwa2100'

import random

class Map_Gen:
    def __init__(self, p_maxX=20, p_maxY=20, p_percentPassable=50, p_bias=(10, 10, 10, 10), p_startPoint=(1, 1),
                 p_legMin=1, p_legMax=10, p_debug=None):
        # define constants
        self._NOT_PASSABLE = 0
        self._PASSABLE = 1
        self._UP = (0, 1)
        self._DOWN = (0, -1)
        self._LEFT = (-1, 0)
        self._RIGHT = (1, 0)
        self._NUMBER_OF_PASSABLE_TILES = int(p_maxX * p_maxY * (p_percentPassable / 100))
        self._MAX_X = p_maxX
        self._MAX_Y = p_maxY
        self._LIMITS = [(0, 0), (0, self._MAX_Y - 1), (self._MAX_X - 1, 0), (self._MAX_X - 1, self._MAX_Y - 1)]
        self._BIAS = p_bias
        self._START_POINT = p_startPoint
        self._LEG_MIN = p_legMin
        self._LEG_MAX = p_legMax

        # define variables
        self.lvl_map = []
        self.entrance = (0, 0)
        self.tunnels = 20
        self.turtlePos = self._START_POINT
        self.turtleDirection = 0
        self.options = []

        # setup
        # Create our blank map to work off of.
        self.createBlankMap()
        self.createMap()
        if p_debug:
            self.drawMap()
            input()

    def MoveTurtle(self, p_move):
        """

        :param p_move: a tuple containing x,y deltas
        :type p_move: tuple(int,int)
        """
        self.turtlePos = self.AddPositions(self.turtlePos, p_move)

    def EditTurtleTile(self, p_flag):
        """

        :param p_flag: the value to store at turtles position
        :type p_flag: int
        """
        self.lvl_map[self.turtlePos[0]][self.turtlePos[1]] = p_flag

    def GetCurrentPositionPassable(self, p_currentPosition):
        """

        :param p_currentPosition: The position you want to check for passable or not.
        :type p_currentPosition: tuple(int,int)
        :return: int
        """
        return int(self.lvl_map[p_currentPosition[0]][p_currentPosition[1]])

    # Check to ensure that the position is within the defined limits of the map. [-1 to keep it off sides]
    def CheckWithinLimits(self, p_postuple):
        if p_postuple[0] > self._MAX_X - 2:
            return False
        if p_postuple[0] < 1:
            return False
        if p_postuple[1] > self._MAX_Y - 2:
            return False
        if p_postuple[1] < 1:
            return False
        return True

    def AddPositions(self, p_tupleA, p_tupleB):
        return tuple(map(sum, zip(p_tupleA, p_tupleB)))

    def LoadBiasOptions(self):
        self.options = []
        for x in range(0, self._BIAS[0]):
            self.options.append(self._LEFT)
        for x in range(0, self._BIAS[1]):
            self.options.append(self._UP)
        for x in range(0, self._BIAS[2]):
            self.options.append(self._RIGHT)
        for x in range(0, self._BIAS[3]):
            self.options.append(self._DOWN)

    # bias is left up right down
    def createMap(self):

        self.LoadBiasOptions()

        # Set entry point position to passable.
        self.lvl_map[1][1] = self._PASSABLE

        iterations = self._NUMBER_OF_PASSABLE_TILES

        # Loop over creation until we have the prescribed number of iterations(passable blocks)
        while iterations > 0:
            # move from start point in random direction.
            self.turtleDirection = random.choice(self.options)
            distance = random.randint(self._LEG_MIN, self._LEG_MAX)
            for x in range(0, distance):
                if self.CheckWithinLimits(self.AddPositions(self.turtlePos, self.turtleDirection)):
                    self.MoveTurtle(self.turtleDirection)
                    self.EditTurtleTile(self._PASSABLE)
                    iterations -= 1

    def GetTgtPosition(self, distance):
        return self.turtlePos[0] + (self.turtleDirection[0] * distance), self.turtlePos[1] + (
                    self.turtleDirection[1] + distance)

    def createBlankMap(self):
        self.lvl_map = []
        for row in range(0, self._MAX_Y):
            self.lvl_map.append(list())
            for col in range(0, self._MAX_X):
                # put walls everywhere
                self.lvl_map[row].append(self._NOT_PASSABLE)

    def drawMap(self):
        rowtoprint = ""
        for row in self.lvl_map:
            for col in row:
                rowtoprint += str(col)
            print(rowtoprint)
            rowtoprint = ""

    def GetLevelMap(self):
        return self.lvl_map

    def GetXLimit(self):
        return self._MAX_X - 1

    def GetYLimit(self):
        return self._MAX_Y - 1

    def DebugGetLevelMap(self):
        self.drawMap(self.lvl_map)
        return self.lvl_map
