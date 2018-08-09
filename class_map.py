
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
def GenLineList(p_currentPos, p_targetPosition, p_minX, p_minY, p_limX, p_limY, p_horizontalFirst=1):
    if CheckWithinLimits(p_targetPosition[0],p_targetPosition[1],p_minX, p_minY, p_limX, p_limY):
      cells = []
      if p_horizontalFirst:
        for x in range(p_currentPos[0],p_targetPosition[0]):
          cells.append((x,p_targetPosition[1]))
        for y in range(p_currentPos[1],p_targetPosition[1]):
          cells.append((p_targetPosition[0],y))
      else:
        for y in range(p_currentPos[1],p_targetPosition[1]):
          cells.append((p_targetPosition[0],y))
        for x in range(p_currentPos[0],p_targetPosition[0]):
          cells.append((x,p_targetPosition[1]))
      return cells

def MoveTurtle(p_currentPos,p_move):
    return (p_currentPos[0] + p_move[0], p_currentPos[1] + p_move[1])

def GetCurrentPositionPassable(p_currentPosition, p_map):
    return int(p_map[p_currentPosition[0]][p_currentPosition[1]])

def CheckWithinLimits(p_posX, p_posY, p_minX, p_minY, p_limX, p_limY):
    if p_posX > p_limX:
      return False
    if p_posX < p_minX:
      return False
    if p_posY > p_limY:
      return False
    if p_posY < p_minY:
      return False
    return True
#bias is left up right down
def createMap(p_maxX=20, p_maxY=20, p_percentPassable=33,p_bias=(10,10,12,12)):
    #define constants
    _NOT_PASSABLE = 0
    _PASSABLE = 1
    _UP = (0,1)
    _DOWN = (0, -1)
    _LEFT = (-1, 0)
    _RIGHT = (1, 0)
    _PERCENT_PASSABLE = p_percentPassable/100
    _MAX_X = p_maxX
    _MAX_Y = p_maxY
    _LIMITS = [(0,0),(0,_MAX_Y), (_MAX_X, 0), (_MAX_X,_MAX_Y)]
    _BIAS = p_bias

    #define variables
    lvl_map=[]
    maxX = 20
    maxY = 20
    Entrence = (0,0)
    tunnels = 20
    #Boss = (random.randint((maxX-random.randint(0-5),maxY-random.randint(0-5)),random.randint(maxX-random.randint(0-5),maxY-random.randint(0-5)))

    options = []
    for x in range(0,p_bias[0]):
      options.append(_LEFT)
    for x in range(0,p_bias[1]):
      options.append(_UP)
    for x in range(0,p_bias[2]):
      options.append(_RIGHT)
    for x in range(0,p_bias[3]):
      options.append(_DOWN)

    lvl_map = createBlankMap(maxX,maxY)
    print("New")
    #Set entry point
    #lvl_map[0][0]="0"
    lvl_map[1][1]="1"

    currentPosition = (1,1)
    
    iterations = int(_MAX_X * _MAX_Y  * _PERCENT_PASSABLE)
    while iterations > 0:
      #print ("Iterations remaining: " + str(iterations),end='\r'
      #move from start point in random direction.
      direction = random.choice(options)
      distance = random.randint(1,4)
      oldPosition = currentPosition
      if distance > 1:
        tgtPos = (currentPosition[0] + (direction[0] * distance), currentPosition[1] + (direction[1] + distance))
        listOfTile = GenLineList(currentPosition, tgtPos, 1, 1, _MAX_X, _MAX_Y, 1)
        for tile in listOfTile:
          lvl_map[tile[0]][tile[1]]
        iterations -= len(listOfTile)
      #print("Iterations rem: " + str(iterations) + " | Direction: " + str(direction),end='\r')
      currentPosition = MoveTurtle(currentPosition,direction)
      #if we hit the walls, lets not count it and move back to the old position.
      if not CheckWithinLimits(currentPosition[0],currentPosition[1],1,1,_MAX_X-1, _MAX_Y-1):
        print(str(currentPosition) + "Iterations rem: " + str(iterations) + " | Direction: " + str(direction) + " REM: HIT LIMIT",end='\r')
        currentPosition = oldPosition
        continue
      #if the current tile is already set to passable, we keep our position but do not count iteration
      if GetCurrentPositionPassable(currentPosition,lvl_map):
        print(str(currentPosition) + "Iterations rem: " + str(iterations) + " | Direction: " + str(direction) + " REM: Tile Already Passable",end='\r')
        continue
      print(str(currentPosition) + "Iterations rem: " + str(iterations) + " | Direction: " + str(direction) + "REM: G2G",end='\r')
      lvl_map[currentPosition[0]][currentPosition[1]] = _PASSABLE
      iterations -= 1
    drawMap(lvl_map)
    input()
    return lvl_map
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
def createBlankMap(maxX, maxY):
    lvl = []
    for row in range(0, maxY):
      lvl.append(list())
      for col in range(0,maxX):
        #put walls everywhere
        lvl[row].append(0)

    drawMap(lvl)
    return lvl

def drawMap(lvl_map):
    rowtoprint = ""
    for row in lvl_map:
      for col in row:
        rowtoprint+=str(col)
      print(rowtoprint)
      rowtoprint=""
