import random
import time
import textwrap
import class_world
import class_player
import class_support
import class_monster
import helper_functions

#defining Variables
running = True
mod_name = ""

def game_over():
  helper_functions.clear_screen()
  print('__  ______  __  __       ____  ______________  ')
  print('\ \/ / __ \/ / / /      / __ \/  _/ ____/ __ \ ')
  print(' \  / / / / / / /      / / / // // __/ / / / / ')
  print(' / / /_/ / /_/ /      / /_/ // // /___/ /_/ /  ')
  print('/_/\____/\____/      /_____/___/_____/_____/   ')
  input('')
  exit()

def ending():
  helper_functions.clear_screen()
  Print_Img("Logo")
  print(" After a long jounery you arive back at Bavaria")
  print("")
  time.sleep(2)
  helper_functions.clear_screen()
  Print_Img("Castle")
  print(" Shortly after ariving in town you head to the castle to give the king back the Crown")
  time.sleep(1)
  helper_functions.clear_screen()
  Print_Img('King')
  print("Greetings King. I have returned with your lost crown", end="\r")
  time.sleep(1)
  print("King: Thank you for your service. It will not be forgoten", end="\r")
  time.sleep(1)
  print("King: Will you please stay with us as the head of my Knights?", end="\r")
  time.sleep(1)
  Print_Img("Fin")
  print('')
  input('')
  exit()

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

#start of the game
Calradia = class_world.gameWorld()
Gen_Map()
Calradia.char_setup()
helper_functions.clear_screen()

#start of the adventer
print('')
print(f'Welcome to the Bavaria, young {Calradia.player.pname}')
print('')
print('.........          /\_[]_/\  ....')
print('......     ___    |] _||_ [| ....')
print('....      /___\    \/ || \/  ....')
print('...      (|0 0|)      ||     ....')
print('..     _   {~}   _ |_P||     ....')
print('..    | /\  ~   /_/   []    .....')
print('...   |_| (____)           ......')   
print('....  \_]/______\        ........') 
print('.....    _\_||_/_       .........')    
print('......  (_,_||_,_))   ...........')
print('We are in need of your help. Yesterday, a goblin stole the king\'s crown.')
print(' We tried to get it back but the Goblin King\' minions are to strong for our guards')
print('')

tmp=input('''
Will you help us?
1 = Yes, I will help!
2 = No thanks, I have better things to do.
''')

if tmp == "2":
  print('This is a game, so you really don\'t have a choice.')
  print('Man up and save the world!!')
  time.sleep(1)
helper_functions.clear_screen()
print('''

Thank you, adventurer. 

Our guards were able to track down the goblin's to a cave up north. 
Many guards have entered, but no one have returned.
We fear the worse for them.   
  ''')

tmp=input('''
Press Enter when you are ready to begin your adventer
  
  ''')
Calradia.Cave_Enter()

#helper_functions.clear_screen()
#We are now in the Cave
while running==True:
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
    class_world.Status_Screen()
  elif tmp.lower() == "w":
    class_world.player.steps += 1
  #move Foward if possible
    helper_functions.clear_screen()
    Y+=1
  elif tmp.lower() == "a":
  #move left if possible
    class_world.player.steps += 1
    helper_functions.clear_screen()
    X-=1
  elif tmp.lower() == "s":
  #move back if possible
    class_world.player.steps += 1
    helper_functions.clear_screen()
    Y-=1
  elif tmp.lower() == "d":
  #move right if possible
    class_world.player.steps += 1
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
  
