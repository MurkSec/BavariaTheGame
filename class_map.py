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
        self._PERCENT_PASSABLE = p_percentPassable / 100
        self._MAX_X = p_maxX
        self._MAX_Y = p_maxY
        self._LIMITS = [(0, 0), (0, self._MAX_Y), (self._MAX_X, 0), (self._MAX_X, self._MAX_Y)]
        self._BIAS = p_bias
        self._START_POINT = p_startPoint

        # define variables
        self.lvl_map = []
        #self.maxX = 20 #should be deprecated
        #self.maxY = 20 #should be deprecated
        self.entrance = (0, 0)
        self.tunnels = 20
        # Boss = (random.randint((maxX-random.randint(0-5),maxY-random.randint(0-5)),random.randint(maxX-random.randint(0-5),maxY-random.randint(0-5)))
        self.turtlePos = self._START_POINT
        self.turtleDirection = 0

        #setup
        # Create our blank map to work off of.
        self.lvl_map = self.createBlankMap()
        self.createMap()

    def GenLineList(self, p_targetPosition, p_horizontalFirst=1):
        if self.CheckWithinLimits(p_targetPosition[0], p_targetPosition[1]):
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

    def MoveTurtle(self, p_currentPos, p_move):
        return (p_currentPos[0] + p_move[0], p_currentPos[1] + p_move[1])

    def GetCurrentPositionPassable(self, p_currentPosition):
        return int(self.lvl_map[p_currentPosition[0]][p_currentPosition[1]])

    # Check to ensure that the position is within the defined limits of the map. [-1 to keep it off sides]
    def CheckWithinLimits(self, p_posX, p_posY):
        if p_posX > self._MAX_X:
            return False
        if p_posX < 1:
            return False
        if p_posY > self._MAX_Y:
            return False
        if p_posY < 1:
            return False
        return True

    # bias is left up right down
    def createMap(self, p_maxX=20, p_maxY=20, p_percentPassable=33, p_bias=(10, 10, 12, 12)):
        

        # load the options list with the possible options available to roll.  This is based off of the biases given during the map setup.
        options = []
        for x in range(0, p_bias[0]):
            options.append(self._LEFT)
        for x in range(0, p_bias[1]):
            options.append(self._UP)
        for x in range(0, p_bias[2]):
            options.append(self._RIGHT)
        for x in range(0, p_bias[3]):
            options.append(self._DOWN)


        # Debug Text :::REMOVE:::
        print("New")
        # Set entry point position to passable.
        self.lvl_map[1][1] = self._PASSABLE

        # Set the number of required passable blocks.
        iterations = int(self._MAX_X * self._MAX_Y * self._PERCENT_PASSABLE)

        # Loop over creation until we have the prescribed number of iterations(passable blocks)
        while iterations > 0:
            # print ("Iterations remaining: " + str(iterations),end='\r'
            # move from start point in random direction.
            self.turtleDirection = random.choice(options)
            distance = random.randint(1, 4)
            oldPosition = self.turtlePos
            if distance > 1:

                listOfTile = self.GenLineList(self.turtlePos, self.GetTgtPosition(distance), 1)
                for tile in listOfTile:
                    self.lvl_map[tile[0]][tile[1]] = self._PASSABLE
                iterations -= len(listOfTile)
            # print("Iterations rem: " + str(iterations) + " | Direction: " + str(direction),end='\r')
            self.turtle = self.MoveTurtle(self.turtlePos, self.turtleDirection)
            # if we hit the walls, lets not count it and move back to the old position.
            if not self.CheckWithinLimits(self.turtlePos[0], self.turtlePos[1]):
                print(str(self.turtlePos) + "Iterations rem: " + str(iterations) + " | Direction: " + str(
                    self.turtleDirection) + " REM: HIT LIMIT", end='\r')
                self.turtlePos = oldPosition
                continue
            # if the current tile is already set to passable, we keep our position but do not count iteration
            if self.GetCurrentPositionPassable(self.turtlePos):
                print(str(self.turtlePos) + "Iterations rem: " + str(iterations) + " | Direction: " + str(
                    self.turtleDirection) + " REM: Tile Already Passable", end='\r')
                continue
            print(str(self.turtlePos) + "Iterations rem: " + str(iterations) + " | Direction: " + str(
                self.turtleDirection) + "REM: G2G", end='\r')
            self.lvl_map[self.turtlePos[0]][self.turtlePos[1]] = self._PASSABLE
            iterations -= 1


    def GetTgtPosition(self, distance):
        return self.turtlePos[0] + (self.turtleDirection[0] * distance), self.turtlePos[1] + (self.turtleDirection[1] + distance)
    '''
        #Cycle throu each Row
        for row in range(1,maxY):
        #Cycle throu each Column
          for col in range(1,maxX):
            found = False
            while not found:
              choice = random.choice(options)
              new_row = (lastChoice[0] + choice[0])
              new_col = (lastChoice[1] + choice[1])
              if (new_row) <= (maxX-1) or (new_row) >= 1:
                if (new_col) <= (maxY-1) or (new_col) >+ 1:
                  found = True
                  lastChoice = choice
            lvl_map[new_row][new_col]="1"
            tunnels -= 1
            if tunnels == 0:
              break
    
        drawMap(lvl_map)
        input("")
        return lvl_map
    '''

    def createBlankMap(self):
        lvl = []
        for row in range(0, self._MAX_Y):
            lvl.append(list())
            for col in range(0, self._MAX_X):
                # put walls everywhere
                lvl[row].append(self._NOT_PASSABLE)
        self.lvl_map = lvl
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