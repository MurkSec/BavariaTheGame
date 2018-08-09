import random

'''
This will return map=[[0,0,0,1,0,0,0,1],
                      [0,0,0,1,0,0,0,1]]

reference place by map[1][2]

'''


def createMap():
    #define variables
    map=[]
    rows=[]
    cols=[]
    maxX = 15
    maxY = 15
    Entrence = (0,0)
    Boss = (random.randint(maxX-random.randint(0-5),maxY-random.randint(0-5)),random.randint(maxX-random.randint(0-5),maxY-random.randint(0-5)))
    
    #Cycle throu each Row
    for row in range(0,maxX):
        #Cycle throu each Column
        for col in range(0,maxY):
            #Add a value to the column
            cols.append("1")
        #Add the Column to the row
        row.append(cols)
    #
    map.append(row)
    [print(row) for row in self.map]
    return map

    
