import random
import time
import textwrap
import class_world
import class_player
import class_support
import class_monster
import helper_functions
import class_graphics
import class_mapgen
import class_map


#defining Variables
mod_name = ""

def Gen_Map():
  #randomly place the boss in the world
  #map grid is 15x15
  #0,0 is reserved for entrence
  Max_X=Calradia.Max_X
  Max_Y=Calradia.Max_Y
  Max_Shops = int((Max_X*Max_Y)*0.05) # 11.25
  Max_BadGuys = int((Max_X*Max_Y)*0.3) #22.5
  Max_Doors = int((Max_X*Max_Y)*0.12) #27
  Max_Fairys = int((Max_X*Max_Y)*0.03) #18
  Max_Walls = int((Max_X*Max_Y)*0.32) #72
  #tunnels will fill in the blanks

  max_slots = Max_X*Max_Y
  Calradia.boss.append((random.randint(int(Max_X/2),Max_Y),random.randint(int(Max_X/2),Max_Y)))
  MaxMobs = random.randint(int(Max_BadGuys*0.75),Max_BadGuys)
  i = 0
  while i < MaxMobs:
    added = False
    #loop to add bad badguys
    while added == False:
      #Loop to check is coordniates are already in another list
      #if not then we add to ours
      tmpLoc = (random.randint(1,Max_Y),random.randint(0,Max_Y))
      #Check it against the Boss list
      #if tmpLoc not in Calradia.boss:
      if tmpLoc != Calradia.boss[0]:
        #not there so we add it
        Calradia.badguys.append(tmpLoc)
        max_slots -= 1
        added = True

    i += 1
  #now that we added mobs and boss
  #we need to add the shops
  i = 0
  while i < Max_Shops:
    added = False
    while added == False:
      tmpLoc = (random.randint(1,Max_Y),random.randint(0,Max_Y))
      if tmpLoc != Calradia.boss[0]:
      #if tmpLoc not in Calradia.boss:
        if tmpLoc not in Calradia.badguys:
          #not there so we add it
          Calradia.shops.append(tmpLoc)
          max_slots -= 1
          added = True
    i+=1
  
  #now that we added mobs, boss, and shops
  #we need to add the Faries
  i = 0
  while i < Max_Fairys:
    added = False
    while added == False:
      tmpLoc = (random.randint(1,Max_Y),random.randint(0,Max_Y))
      if tmpLoc != Calradia.boss[0]:
      #if tmpLoc not in Calradia.boss:
        if tmpLoc not in Calradia.badguys:
          if tmpLoc not in Calradia.shops:
            #not there so we add it
            Calradia.fairys.append(tmpLoc)
            max_slots -= 1
            added = True
    i+=1
  #now that we added mobs, boss, shops, and Faries
  #we need to add a special treasure room
  i = 0
  added = False
  while added == False:
    tmpLoc = (random.randint(1,Max_Y),random.randint(0,Max_Y))
    if tmpLoc != Calradia.boss[0]:
    #if tmpLoc not in Calradia.boss:
      if tmpLoc not in Calradia.badguys:
        if tmpLoc not in Calradia.shops:
          if tmpLoc not in Calradia.fairys:
            #not there so we add it
            Calradia.treasure.append(tmpLoc)
            max_slots -= 1
            added = True
  #now that we added mobs, boss, shops, Faries, and treasure
  #we need to add the doors
  i = 0
  while i < Max_Doors:
    added = False
    while added == False:
      tmpLoc = (random.randint(1,Max_Y),random.randint(0,Max_Y))
      if tmpLoc != Calradia.boss[0]:
      #if tmpLoc not in Calradia.boss:
        if tmpLoc not in Calradia.badguys:
          if tmpLoc not in Calradia.shops:
            if tmpLoc not in Calradia.fairys:
              if tmpLoc not in Calradia.treasure:
                #not there so we add it
                Calradia.doors.append(tmpLoc)
                max_slots -= 1
                added = True
    i+=1
  #now that we added mobs, boss, shops, Faries,treasure and doors
  #we need to add the walls
  i = 0
  while i < Max_Walls:
    added = False
    while added == False:
      tmpLoc = (random.randint(1,Max_Y),random.randint(0,Max_Y))
      if tmpLoc != Calradia.boss[0]:
      #if tmpLoc not in Calradia.boss:
        if tmpLoc not in Calradia.badguys:
          if tmpLoc not in Calradia.shops:
            if tmpLoc not in Calradia.fairys:
              if tmpLoc not in Calradia.treasure:
               if tmpLoc not in Calradia.doors:
                  #not there so we add it
                  Calradia.walls.append(tmpLoc)
                  max_slots -= 1
                  added = True
    i+=1
  #now that we added mobs, boss, shops, Faries,treasure,doors and walls
  #we need to add the tunnels

  X = 0
  cnt = 0
  while X <= Max_X:
    Y = Max_Y
    while Y >= 0:
      tmpLoc = (X,Y)
      if tmpLoc != Calradia.boss[0]:
      #if tmpLoc not in Calradia.boss:
        if tmpLoc not in Calradia.badguys:
          if tmpLoc not in Calradia.shops:
            if tmpLoc not in Calradia.fairys:
              if tmpLoc not in Calradia.treasure:
                if tmpLoc not in Calradia.doors:
                 if tmpLoc not in Calradia.walls:
                   if tmpLoc != Calradia.entrence:
                    Calradia.tunnels.append(tmpLoc)
                    cnt +=1 
      Y-=1
    X+=1


def Move_Char(X,Y):
  #Checks for valid movement
  if X < 0:
    X = 0
  elif Y < 0:
    Y = 0
  elif X > Calradia.Max_X:
    X = Calradia.Max_X
  elif Y > Calradia.Max_Y:
    Y = Calradia.Max_Y

  ckCord = (X,Y)
  if ckCord in Calradia.boss:
    return "Boss"
  elif ckCord == Calradia.entrence:
    return "Cave_Enter"
  elif ckCord == Calradia.badKilled:
    return "Cave_tunnel"
  elif ckCord in Calradia.badguys:
    return "Cave_Encounter"
  elif ckCord in Calradia.shops:
    return "Cave_shop"
  elif ckCord in Calradia.fairys:
    return "Cave_fairy"
  elif ckCord in Calradia.treasure:
    return "Treasure"
  elif ckCord in Calradia.doors:
    return "Cave_Door"
  elif ckCord in Calradia.walls:
    return "Cave_Wall"
  elif ckCord in Calradia.tunnels:
    return "Cave_tunnel"


CHARACTER_TILES = {'void': ' ', 'floor': '.', 'wall': '#'}

class Generator():
    def __init__(self, width=64, height=64, max_rooms=15, min_room_xy=5, max_room_xy=10, rooms_overlap=False, random_connections=1, random_spurs=3, tiles=CHARACTER_TILES):
        self.width = width
        self.height = height
        self.max_rooms = max_rooms #default rooms set to 15
        self.min_room_xy = min_room_xy #default set to 5
        self.max_room_xy = max_room_xy #default set to 10
        self.rooms_overlap = rooms_overlap #default set to False
        self.random_connections = random_connections #default set to 1
        self.random_spurs = random_spurs #3 default set to 3
        self.tiles = CHARACTER_TILES  #default set at top
        self.level = []
        self.room_list = []
        self.corridor_list = []
        self.tiles_level = []

    def gen_room(self):
        x, y, w, h = 0, 0, 0, 0
        w = random.randint(self.min_room_xy, self.max_room_xy)
        h = random.randint(self.min_room_xy, self.max_room_xy)
        x = random.randint(1, (self.width - w - 1))
        y = random.randint(1, (self.height - h - 1))
        return [x, y, w, h]

    def room_overlapping(self, room, room_list):
        x = room[0]
        y = room[1]
        w = room[2]
        h = room[3]
        for current_room in room_list:
            # The rectangles don't overlap if
            # one rectangle's minimum in some dimension
            # is greater than the other's maximum in
            # that dimension.
            if (x < (current_room[0] + current_room[2]) and
                current_room[0] < (x + w) and
                y < (current_room[1] + current_room[3]) and
                current_room[1] < (y + h)):
                return True
        return False

    def corridor_between_points(self, x1, y1, x2, y2, join_type='either'):
        if x1 == x2 and y1 == y2 or x1 == x2 or y1 == y2:
            return [(x1, y1), (x2, y2)]
        else:
            # 2 Corridors
            # NOTE: Never randomly choose a join that will go out of bounds
            # when the walls are added.
            join = None
            if join_type is 'either' and set([0, 1]).intersection(
                 set([x1, x2, y1, y2])):
                join = 'bottom'
            elif join_type is 'either' and set([self.width - 1,
                 self.width - 2]).intersection(set([x1, x2])) or set(
                 [self.height - 1, self.height - 2]).intersection(
                 set([y1, y2])):
                join = 'top'
            elif join_type is 'either':
                join = random.choice(['top', 'bottom'])
            else:
                join = join_type
            if join is 'top':
                return [(x1, y1), (x1, y2), (x2, y2)]
            elif join is 'bottom':
                return [(x1, y1), (x2, y1), (x2, y2)]
 
    def join_rooms(self, room_1, room_2, join_type='either'):
        # sort by the value of x
        sorted_room = [room_1, room_2]
        sorted_room.sort(key=lambda x_y: x_y[0])
        x1 = sorted_room[0][0]
        y1 = sorted_room[0][1]
        w1 = sorted_room[0][2]
        h1 = sorted_room[0][3]
        x1_2 = x1 + w1 - 1
        y1_2 = y1 + h1 - 1
        x2 = sorted_room[1][0]
        y2 = sorted_room[1][1]
        w2 = sorted_room[1][2]
        h2 = sorted_room[1][3]
        x2_2 = x2 + w2 - 1
        y2_2 = y2 + h2 - 1
        # overlapping on x
        if x1 < (x2 + w2) and x2 < (x1 + w1):
            jx1 = random.randint(x2, x1_2)
            jx2 = jx1
            tmp_y = [y1, y2, y1_2, y2_2]
            tmp_y.sort()
            jy1 = tmp_y[1] + 1
            jy2 = tmp_y[2] - 1
            corridors = self.corridor_between_points(jx1, jy1, jx2, jy2)
            self.corridor_list.append(corridors)
        # overlapping on y
        elif y1 < (y2 + h2) and y2 < (y1 + h1):
            if y2 > y1:
                jy1 = random.randint(y2, y1_2)
                jy2 = jy1
            else:
                jy1 = random.randint(y1, y2_2)
                jy2 = jy1
            tmp_x = [x1, x2, x1_2, x2_2]
            tmp_x.sort()
            jx1 = tmp_x[1] + 1
            jx2 = tmp_x[2] - 1
            corridors = self.corridor_between_points(jx1, jy1, jx2, jy2)
            self.corridor_list.append(corridors)
        # no overlap
        else:
            join = None
            if join_type is 'either':
                join = random.choice(['top', 'bottom'])
            else:
                join = join_type
            if join is 'top':
                if y2 > y1:
                    jx1 = x1_2 + 1
                    jy1 = random.randint(y1, y1_2)
                    jx2 = random.randint(x2, x2_2)
                    jy2 = y2 - 1
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'bottom')
                    self.corridor_list.append(corridors)
                else:
                    jx1 = random.randint(x1, x1_2)
                    jy1 = y1 - 1
                    jx2 = x2 - 1
                    jy2 = random.randint(y2, y2_2)
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'top')
                    self.corridor_list.append(corridors)
            elif join is 'bottom':
                if y2 > y1:
                    jx1 = random.randint(x1, x1_2)
                    jy1 = y1_2 + 1
                    jx2 = x2 - 1
                    jy2 = random.randint(y2, y2_2)
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'top')
                    self.corridor_list.append(corridors)
                else:
                    jx1 = x1_2 + 1
                    jy1 = random.randint(y1, y1_2)
                    jx2 = random.randint(x2, x2_2)
                    jy2 = y2_2 + 1
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'bottom')
                    self.corridor_list.append(corridors)

    def gen_level(self):
        # build an empty dungeon, blank the room and corridor lists
        for i in range(self.height):
            self.level.append(['stone'] * self.width)
        self.room_list = []
        self.corridor_list = []
        max_iters = self.max_rooms * 5
        for a in range(max_iters):
            #generate new room
            tmp_room = self.gen_room()
            if self.rooms_overlap or not self.room_list:
                #if it doesn't overlap then added it
                self.room_list.append(tmp_room)
            else:
                #add new remove to temp list
                #without check if it overlaps
                tmp_room = self.gen_room()
                tmp_room_list = self.room_list[:]
                if self.room_overlapping(tmp_room, tmp_room_list) is False:
                    self.room_list.append(tmp_room)
            #Max number of rooms so we quit
            if len(self.room_list) >= self.max_rooms:
                break
        # connect the rooms
        for a in range(len(self.room_list) - 1):
            self.join_rooms(self.room_list[a], self.room_list[a + 1])
        # do the random joins
        for a in range(self.random_connections):
            room_1 = self.room_list[random.randint(0, len(self.room_list) - 1)]
            room_2 = self.room_list[random.randint(0, len(self.room_list) - 1)]
            self.join_rooms(room_1, room_2)
        # do the spurs
        for a in range(self.random_spurs):
            room_1 = [random.randint(2, self.width - 2), random.randint(
                     2, self.height - 2), 1, 1]
            room_2 = self.room_list[random.randint(0, len(self.room_list) - 1)]
            self.join_rooms(room_1, room_2)
        # fill the map
        # paint rooms
        for room_num, room in enumerate(self.room_list):
            for b in range(room[2]):
                for c in range(room[3]):
                    self.level[room[1] + c][room[0] + b] = 'floor'
        # paint corridors
        for corridor in self.corridor_list:
            x1, y1 = corridor[0]
            x2, y2 = corridor[1]
            for width in range(abs(x1 - x2) + 1):
                for height in range(abs(y1 - y2) + 1):
                    self.level[min(y1, y2) + height][
                        min(x1, x2) + width] = 'floor'
        # paint corridors
            if len(corridor) == 3:
                x3, y3 = corridor[2]
                for width in range(abs(x2 - x3) + 1):
                    for height in range(abs(y2 - y3) + 1):
                        self.level[min(y2, y3) + height][
                            min(x2, x3) + width] = 'floor'
        # paint the walls
        for row in range(1, self.height - 1):
            for col in range(1, self.width - 1):
                if self.level[row][col] == 'floor':
                    if self.level[row - 1][col - 1] == 'stone':
                        self.level[row - 1][col - 1] = 'wall'
                    if self.level[row - 1][col] == 'stone':
                        self.level[row - 1][col] = 'wall'
                    if self.level[row - 1][col + 1] == 'stone':
                        self.level[row - 1][col + 1] = 'wall'
                    if self.level[row][col - 1] == 'stone':
                        self.level[row][col - 1] = 'wall'
                    if self.level[row][col + 1] == 'stone':
                        self.level[row][col + 1] = 'wall'
                    if self.level[row + 1][col - 1] == 'stone':
                        self.level[row + 1][col - 1] = 'wall'
                    if self.level[row + 1][col] == 'stone':
                        self.level[row + 1][col] = 'wall'
                    if self.level[row + 1][col + 1] == 'stone':
                        self.level[row + 1][col + 1] = 'wall'

    def gen_tiles_level(self):
        for row_num, row in enumerate(self.level):
            tmp_tiles = []
            for col_num, col in enumerate(row):
                if col == 'stone':
                    tmp_tiles.append(self.tiles['stone'])
                if col == 'floor':
                    tmp_tiles.append(self.tiles['floor'])
                if col == 'wall':
                    tmp_tiles.append(self.tiles['wall'])
            self.tiles_level.append(''.join(tmp_tiles))
        print('Room List: ', self.room_list)
        print('\nCorridor List: ', self.corridor_list)
        [print(row) for row in self.tiles_level]
        #return self.room_list, self.corridor_list, self.tiles_level

if __name__ == '__main__':
    gen = Generator()
    gen.gen_level()
    gen.gen_tiles_level()

#start of the game
Calradia = class_world.gameWorld()
while Calradia.running == True:
  new_lvl = []
  new_lvl = class_map.createMap()
  #lvl = Generator()
  #print(list(lvl))
  Gen_Map()
  Calradia.char_setup()
  helper_functions.clear_screen()

  #start of the adventer
  print('')
  print(f'Welcome to Bavaria, young {Calradia.player.pname}')
  print('')
  Calradia.graphics.CallArtByName("Dwarf").ShowArt()
  print('')
  print('We are in need of your help. Yesterday, a goblin stole the king\'s crown.')
  print(' We tried to get it back but the Goblin King\' minions are to strong for our guards')
  print('')

  tmp=input('''
  Will you help us?
  1 = Yes, I will help!
  2 = No thanks, I have better things to do.
  ''')

  if tmp == "2":
    print("This is a game, so you really don't have a choice.")
    print('Man up and save the world!!')
    time.sleep(1)
  helper_functions.clear_screen()
  print('''

  Thank you, Adventurer. 

  Our guards were able to track down the goblins to a cave up north. 
  Many guards have entered, but not one has returned.
  We fear the worst for them.   
    ''')

  tmp=input('''
  Press Enter when you are ready to begin your adventure!
    
    ''')
  Calradia.Cave_Enter()
  Calradia.started = True
  #helper_functions.clear_screen()
  #We are now in the Cave
  while Calradia.started==True:
    X = 0
    Y = 0

    tmp = input(textwrap.dedent('''
    Options:

    Press C to see stats
    Press W to move Foward
    Press A to move Left
    Press S to move Back
    Press D to move Right
    
    '''))
    if tmp.lower() == "c":
    #Show the stats/item screen
      helper_functions.clear_screen()
      Calradia.Stats()
      Calradia.Status_Screen()
    elif tmp.lower() == "w":
      #class_world.player.steps += 1
    #move Foward if possible
      helper_functions.clear_screen()
      Y+=1
    elif tmp.lower() == "a":
    #move left if possible
      #class_world.player.steps += 1
      helper_functions.clear_screen()
      X-=1
    elif tmp.lower() == "s":
    #move back if possible
      #class_world.player.steps += 1
      helper_functions.clear_screen()
      Y-=1
    elif tmp.lower() == "d":
    #move right if possible
      #class_world.player.steps += 1
      helper_functions.clear_screen()
      X+=1
    elif tmp.lower() == "debug":
      Calradia.Debug_Menu()


    #Check X field
    if Calradia.position[0] < 0:
      Calradia.position = (0,Calradia.position[1])
    if Calradia.position[0] > Calradia.Max_X:
      Calradia.position = (Calradia.Max_X,Calradia.position[1])
    if (Calradia.position[0]+X) < 0:
      X=0
    if (Calradia.position[0]+X) > Calradia.Max_X:
      X=Calradia.Max_X

    #Check Y field
    if Calradia.position[1] < 0:
      Calradia.position = (Calradia.position[0],0)
    if Calradia.position[1] > Calradia.Max_Y:
      Calradia.position = (Calradia.position[0],Calradia.Max_Y)
    if (Calradia.position[1]+Y) < 0:
      Y=0
    if (Calradia.position[1]+Y) > Calradia.Max_Y:
      Y=Calradia.Max_Y
    
    tmpResult = Move_Char(Calradia.position[0]+X , Calradia.position[1]+Y)
    Calradia.position = Calradia.position[0]+X , Calradia.position[1]+Y

    #Check again for correct Value
    if Calradia.position[1] < 0:
      Calradia.position = (Calradia.position[0],0)
    if Calradia.position[1] > Calradia.Max_X:
      Calradia.position = (Calradia.position[0],Calradia.Max_X)
    if Calradia.position[0] < 0:
      Calradia.position = (0,Calradia.position[1])
    if Calradia.position[0] > Calradia.Max_X:
      Calradia.position = (Calradia.Max_X,Calradia.position[1])


    if tmpResult == "Cave_Encounter":
      Calradia.Cave_Encounter()
    elif tmpResult == "Cave_Enter":
      Calradia.Cave_Enter()
    elif tmpResult == "Cave_Door":
      Calradia.Cave_Door()
    elif tmpResult == "Cave_Wall":
      Calradia.Cave_Wall()
    elif tmpResult == "Cave_tunnel":
      Calradia.Cave_tunnel()
    elif tmpResult == "Cave_fairy":
      Calradia.Cave_fairy()
    elif tmpResult == "Cave_shop":
      Calradia.Cave_shop()
    elif tmpResult == "Boss":
      Calradia.Cave_Boss()
    elif tmpResult == "Treasure":
      Calradia.Cave_Treasure()
    else:
      Calradia.Cave_tunnel()
    
