import random

'''
This will return map=[[0,0,0,1,0,0,0,1],
                      [0,0,0,1,0,0,0,1]]

reference place by map[1][2]


0 = Entry//
1 = Tunnel
2 = Wall

0 = not passable
1 = passable
'''


class Map_Gen:
    def __init__(self, p_maxX=20, p_maxY=20, p_percentPassable=33, p_bias=(10, 10, 12, 12), p_startPoint = (1,1)):
        # define constants
        self._NOT_PASSABLE = 0
        self._PASSABLE = 1
        self._UP = (0, 1)
        self._DOWN = (0, -1)
        self._LEFT = (-1, 0)
        self._RIGHT = (1, 0)
        self._NUMBER_OF_PASSABLE_TILES = int(p_maxX * p_maxY * (p_percentPassable/100))
        self._MAX_X = p_maxX
        self._MAX_Y = p_maxY
        self._LIMITS = [(0, 0), (0, self._MAX_Y), (self._MAX_X, 0), (self._MAX_X, self._MAX_Y)]
        self._BIAS = p_bias
        self._START_POINT = p_startPoint

        # define variables
        self.lvl_map = []
        self.entrance = (0, 0)
        self.tunnels = 20
        self.turtlePos = self._START_POINT
        self.turtleDirection = 0
        self.options = []

        #setup
        # Create our blank map to work off of.
        self.createBlankMap()
        self.createMap()

    def GenLineList(self, p_targetPosition, p_horizontalFirst=1):
        if self.CheckWithinLimits(p_targetPosition):
            cells = []
            if p_horizontalFirst:
                for x in range(self.turtlePos[0], p_targetPosition[0]):
                    cells.append((x, p_targetPosition[1]))
                for y in range(self.turtlePos[1], p_targetPosition[1]):
                    cells.append((p_targetPosition[0], y))
            else:
                for y in range(self.turtlePos[1], p_targetPosition[1]):
                    cells.append((p_targetPosition[0], y))
                for x in range(self.turtlePos[0], p_targetPosition[0]):
                    cells.append((x, p_targetPosition[1]))
            return cells

    def MoveTurtle(self, p_move):
        self.turtlePos += p_move

    def EditTurtleTile(self, p_flag):
        self.lvl_map[self.turtlePos[0]][self.turtlePos[1]] = p_flag

    def GetCurrentPositionPassable(self, p_currentPosition):
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
        return tuple(map(sum,zip(p_tupleA,p_tupleB)))

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

        # Debug Text :::REMOVE:::
        print("New")

        # Set entry point position to passable.
        self.lvl_map[1][1] = self._PASSABLE

        iterations = self._NUMBER_OF_PASSABLE_TILES

        # Loop over creation until we have the prescribed number of iterations(passable blocks)
        while iterations > 0:
            print(str(iterations))
            # print ("Iterations remaining: " + str(iterations),end='\r'
            # move from start point in random direction.
            self.turtleDirection = random.choice(self.options)
            distance = random.randint(1, 4)
            #oldPosition = self.turtlePos
            for x in range(0, distance):
                if self.CheckWithinLimits(self.AddPositions(self.turtlePos, self.turtleDirection)):
                    self.MoveTurtle(self.turtleDirection)
                    self.EditTurtleTile(self._PASSABLE)
                    iterations -= 1
            # if distance > 1:
            #     listOfTile = self.GenLineList(self.GetTgtPosition(distance), 1)
            #     if listOfTile:
            #         for tile in listOfTile:
            #             if self.lvl_map != self._PASSABLE:
            #                 self.lvl_map[tile[0]][tile[1]] = self._PASSABLE
            #             self.turtlePos = (tile[0], tile[1])
            #                 iterations -= 1
            # # print("Iterations rem: " + str(iterations) + " | Direction: " + str(direction),end='\r')
            # self.MoveTurtle(self.turtleDirection)
            # if we hit the walls, lets not count it and move back to the old position.
            # if not self.CheckWithinLimits(self.turtlePos[0], self.turtlePos[1]):
            #     print(str(self.turtlePos) + "Iterations rem: " + str(iterations) + " | Direction: " + str(
            #         self.turtleDirection) + " REM: HIT LIMIT", end='\r')
            #     self.turtlePos = oldPosition
            #     continue
            # # if the current tile is already set to passable, we keep our position but do not count iteration
            # if self.GetCurrentPositionPassable(self.turtlePos):
            #     print(str(self.turtlePos) + "Iterations rem: " + str(iterations) + " | Direction: " + str(
            #         self.turtleDirection) + " REM: Tile Already Passable", end='\r')
            #     continue
            # print(str(self.turtlePos) + "Iterations rem: " + str(iterations) + " | Direction: " + str(
            #     self.turtleDirection) + "REM: G2G", end='\r')
            # self.lvl_map[self.turtlePos[0]][self.turtlePos[1]] = self._PASSABLE
            # iterations -= 1


    def GetTgtPosition(self, distance):
        return self.turtlePos[0] + (self.turtleDirection[0] * distance), self.turtlePos[1] + (self.turtleDirection[1] + distance)

    def createBlankMap(self):
        self.lvl_map = []
        for row in range(0, self._MAX_Y):
            self.lvl_map.append(list())
            for col in range(0, self._MAX_X):
                # put walls everywhere
                self.lvl_map[row].append(self._NOT_PASSABLE)
        #DEBUG ***REMOVE ME***
        self.drawMap()


    def drawMap(self):
        rowtoprint = ""
        for row in self.lvl_map:
            for col in row:
                rowtoprint += str(col)
            print(rowtoprint)
            rowtoprint = ""

    def GetLevelMap(self):
        return self.lvl_map

    def DebugGetLevelMap(self):
        self.drawMap(self.lvl_map)
        # Debug :::REMOVE ME:::
        input()
        return self.lvl_map
