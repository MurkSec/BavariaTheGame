import random

'''
This will return map=[[0,0,0,1,0,0,0,1],
                      [0,0,0,1,0,0,0,1]]

reference place by map[1][2]

'''


def createMap():
    #define variables
    lvl_map=[]
    rows=[]
    cols=[]
    maxX = 15
    maxY = 15
    Entrence = (0,0)
    #Boss = (random.randint(maxX-random.randint(0-5),maxY-random.randint(0-5)),random.randint(maxX-random.randint(0-5),maxY-random.randint(0-5)))
    
    #Cycle throu each Row
    for row in range(0,maxY):
        #Cycle throu each Column
        for col in range(0,maxX):
            #Add a value to the column
            #cols.append("1")
            lvl_map[row].append("1")
        #Add the Column to the row
        #rows.append(cols)
    #
    #lvl_map.append(row)
    #[print(row) for row in map]
    drawMap(lvl_map)
    input("")
    return lvl_map

def drawMap(lvl_map):
    for row in lvl_map:
      for col in row:
        print(col)
        #for col in row:
        #    print(col)
      
      
    
