

import random
import time
import textwrap
import class_player
import class_support
import class_monster


running = True
mod_name = ""

def clear_screen():
  print('\033[H\033[J')
  time.sleep(0.1)




def game_over():
  clear_screen()
  print('__  ______  __  __       ____  ______________  ')
  print('\ \/ / __ \/ / / /      / __ \/  _/ ____/ __ \ ')
  print(' \  / / / / / / /      / / / // // __/ / / / / ')
  print(' / / /_/ / /_/ /      / /_/ // // /___/ /_/ /  ')
  print('/_/\____/\____/      /_____/___/_____/_____/   ')
  input('')
  exit()

def ending():
  clear_screen()
  Print_Img("Logo")
  print(" After a long jounery you arive back at Bavaria")
  print("")
  time.sleep(2)
  clear_screen()
  Print_Img("Castle")
  print(" Shortly after ariving in town you head to the castle to give the king back the Crown")
  time.sleep(1)
  clear_screen()
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


class gameWorld:
  #Initialize our game world
  def __init__(self):
    self.position = (0,0) #location x,y
    self.Max_X = 15
    self.Max_Y = 15
    self.player = class_player.player()
    self.encounters = 0
    self.BossFound = False
    self.BossKilled = False
    self.treasurefound = False
    self.enemy = ""
    
    #defining map list
    self.walls = []
    self.tunnels = []
    self.fairys = []
    self.shops = []
    self.badguys = []
    self.badKilled = []
    self.doors = []
    self.boss = []
    self.treasure = []
    self.entrence = (0,0)


    #Creating Item list
    self.Spells= [class_support.Spell("Cure", 1, "Heal", 15, 30), class_support.Spell("Fireball", 1, "Atk", 15, 15), class_support.Spell("Str Up", 1, "Buff", 20, 5)]
    self.weapons = [class_support.Weapon("Short Sword", 5, 10, "sword"), class_support.Weapon("Brass Knuckles", 10, 14, "bare"), class_support.Weapon("Wooden Staff", 5, 10, "staff"), class_support.Weapon("Rapier", 9, 5, "sword"), class_support.Weapon("Long Sword", 20, 10, "sword"), class_support.Weapon("light Axe", 28, 15, "axe"), class_support.Weapon("Small Knife", 5, 15, "knife"), class_support.Weapon("Stick", 1, 3, "knife")]
    self.armors = [class_support.Armor("Cloth Armor", 10, 5, "cloth"), class_support.Armor("Shirt", 10, 3, "cloth"), class_support.Armor("Lether Armor", 15, 8, "lether"), class_support.Armor("Robe", 10, 3, "cloth"), class_support.Armor("Cover-all", 5, 7, "cloth")]
    self.items = [class_support.Item("Potion", "Heal", 1, 30), class_support.Item("Ether", "Heal", 1, 25),class_support.Item("Kings Crown", "Key", 1), class_support.Item('Door Key', "Consumable", 1), class_support.Item("Skull Key", "Consumable", 1)]
    self.moblist = []
    self.addMonster("Goblin", 1, 20, 8, "Goblin")
    self.addMonster("Red Goblin", 2,23, 5, "Goblin")
    self.addMonster("Blue Goblin", 3,23, 6, "Goblin")
    self.addMonster("Green Goblin", 2,15, 7, "Goblin")
    self.addMonster("Goblin Minion", 1,20, 9, "Goblin")
    self.addMonster("Brown Recluse", 2, 14, 10, "Spider")
    self.addMonster("House Spider", 1, 13, 8, "Spider")
    self.addMonster("Black Widow", 3, 25, 15, "Spider")
    self.addMonster("Goblin King", 5, 70, 25, "Boss")

  def addMonster(self, pn, plvl, php_top, ps_top, pTyp):
    #Add a new monstor to our list
    for m in self.moblist:
      if m.mName == pn:
        return False
    self.moblist.append(class_monster.monster(pn, plvl, php_top, ps_top, pTyp))
    return True

  def game_hud(self):
    #Normal HUD
    print(f'Name : {self.player.pname}        Lvl : {self.player.lvl}     Exp : {self.player.exp}')
    print(f'HP : {self.player.health}/{self.player.max_health}      Battles Left: {len(self.badguys)}    Gold : {self.player.gold}')
    #Mage HUD
    #requires additional MP stuff
    if self.player.pclass == "Mage":
      print(f'MP : {self.player.mp}/{self.player.max_mp}')

    #Check if there is anything in the inventory
    if not len(self.player.inv):
      print("Items : None")
    else:
      tmpStr = ""
      for item in self.player.inv:
        if tmpStr == "":
          tmpStr += (item.iname)+ ", "
        else:
          tmpStr += (item.iname + ", ")
      print('Items : ' + tmpStr)
    print(f'Location: {self.position}     Boss Loc: {self.boss[0]}')

  def GiveItem(self, iname, iAmount=1):
    #Check to see if player already has the Item
    for item in self.player.inv:
      if item.iname == iname:
        if item.itype != "Key":
          #Update Amount
          item.iamount += iAmount
          return True
    #couldn't find the item so we are going to add it
    for item in self.items:
      if item.iname == iname:
        self.player.inv.append(class_support.Item(item.iname, item.itype, iAmount, item.iDmg))
        return True    
 
  def RemoveItem(self, pn, pA=1):
    #Remove an item from our inventory
    for i in self.player.inv:
      if i.iname == pn:
        if i.iamount > pA:
          i.iamount -= pA
        else:
          del self.player.inv[self.GetItemIDbyName(pn)]
        return True
    return False

  def GetItemIDbyName(self, pn):
    for x,m in enumerate(self.inv):
      if m.iname == pn:
        return x
    return -1

  def char_setup(self):
    finished = False
    while finished == False:
      #Setup Character
      clear_screen()
      self.player.pname=input('Please enter your name')
      clear_screen()
      print('         Please choice your class')
      print('')
      print('')
      print('1 = Fighter')
      print('2 = Monk')
      print('3 = Thief')
      print('4 = Mage')
      print('')
      print('')
      tmp = input('')

      if tmp == "1":
        #Figher class
        clear_screen()
        self.player.strength=random.randint(8,13)
        self.player.pclass = "Fighter"
        weapon = "Short Sword"
        armor = "Cloth Armor"
        health = 35
        Ev = 8
        Acc = 45
      elif tmp == "2":
        #Monk Class
        clear_screen()
        self.player.strength=random.randint(7,10)
        self.player.pclass = "Monk"
        weapon = "Brass Knuckles"
        armor = "Shirt"
        health = 25
        Ev = 12
        Acc = 35
      elif tmp == "3":
        #Thief Class
        clear_screen()
        self.player.pclass = "Thief"
        weapon = "Small Knife"
        armor = "Lether Armor"
        health = 15
        Ev = 20
        Acc = 30
        self.player.strength=random.randint(5,8)
      elif tmp == "4":
        #Mage Class
        self.player.pclass = "Mage"
        health = 15
        Ev = 12
        Acc = 20
        weapon = "Wooden Staff"
        armor = "Robe"
        self.player.max_mp = 30
        self.player.mp = self.player.max_mp
        self.player.strength=random.randint(4,6)
      else:
        #User didn't choice a class so we will assign open
        #They get a Loser Class
        print("""
        Guess you didn't want to choice a class. 
        Well i will choice for you slacker!
        """)
        self.player.pclass = "Loser"
        self.player.strength = random.randint(1,3)
        weapon = "Stick"
        armor = "Cover-all"
        health = 10
        Ev = 5
        Acc = 5
      #Display to the user what they choose
      if self.player.pname != "GOD":
        self.player.health = health
        self.player.max_health = health
        self.player.Evasion = Ev
        self.player.Accuracy = Acc
        for item in self.weapons:
            if item.wname == weapon:
              wpn = item
        self.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        for item in self.armors:
            if item.aname == armor:
              amn = item
        self.addArmor(amn.aname,amn.arate,amn.aweight, amn.aType)
        self.player.inv.clear()
      else:
        self.GiveItem("Door Key", 1)
        self.GiveItem("Skull Key", 1)
        self.GiveItem("Potion", 10)
        self.GiveItem("Ether", 10)
        self.addSpell("Cure")
        self.addSpell("Fireball")
        self.player.health = 60
        self.player.max_health = self.player.health
        self.player.Evasion = 40
        self.player.Accuracy = 40
        self.player.strength = 25
        for item in self.weapons:
            if item.wname == weapon:
              wpn = item
        self.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        for item in self.armors:
            if item.aname == armor:
              amn = item
        self.addArmor(amn.aname,amn.arate,amn.aweight, amn.aType)
      clear_screen()
      print("")
      print(f'You choose :')
      print(f"Name: {self.player.pname}")
      print(f"Class: {self.player.pclass}")
      print(f"Health: {self.player.health}/{self.player.max_health}")
      if self.player.pclass == "Mage":
        print(f"Mana: {self.player.mp}/{self.player.max_mp}")
      print(f"Evasion: {self.player.Evasion}   Accuracy: {self.player.Accuracy}")
      print(f"Strength: {self.player.strength} ")
      print(f"Weapon: {self.player.Weapon[0].wname}  Atk rate: {self.player.Weapon[0].watk}")
      print(f"Armor: {self.player.Armor[0].aname}  Def rate: {self.player.Armor[0].arate}")
      tmp = input("Do you want to reroll your Character? y/n")
      if tmp.lower() != "y":
        finished = True

  def GetRandomMonster(self):
    return random.choice(self.moblist)

  def GetMonsterIDbyName(self, pn):
    for x,m in enumerate(self.moblist):
      if m.mName == pn:
        return x
    return -1
  
  def GetMonsterByID(self, pid):
    if pid > -1 and pid <= len(self.moblist):
      return self.moblist[pid]
    else:
      return -1

  def GetMonsterbyName(self, pn):
    for m in self.moblist:
      if m.mName == pn:
        return m
    return False

  def ResMonsterbyName(self, pn):
    for m in self.moblist:
      if m.mName == pn:
        m.health = m.max_health
        return True
    return False

  def addArmor(self, armN, armRate, armwg, armType):
    #add Armor to our slot
    if len(self.player.Armor) > 0:
      self.player.Armor[0].aname = armN
      self.player.Armor[0].arate = armRate
      self.player.Armor[0].aweight = armwg
      self.player.Armor[0].aType = armType
      return True
    else:
      self.player.Armor.append(class_support.Armor(armN, armRate, armwg, armType))
      return True

  def addWeapon(self, wn, watk, whit, wType):
    #add an Weapons to our slot
    if len(self.player.Weapon) > 0:
      self.player.Weapon[0].wname = wn
      self.player.Weapon[0].watk = watk
      self.player.Weapon[0].w_hit = whit
      self.player.Weapon[0].wType = wType
      return True
    else:
      self.player.Weapon.append(class_support.Weapon(wn, watk, whit, wType))
      return True

  def addSpell(self, sname):
    #Check to see if player already has the Spell
    for spell in self.player.Spells:
      if spell.sname == sname:
        #Upgrade Spell
        if spell.slevel <= 9:
          spell.slevel += 1
          print(f" You have Upgraded your {sname} spell to {spell.slevel}!")
          spell.sCost += (spell.slevel*2)
          spell.sDmg += (spell.slevel*int(random.randint(1,6)))
          return True
        return False
    #couldn't find the spell so we are going to add it
    for spell in self.Spells:
      if spell.sname == sname:
        self.player.Spells.append(class_support.Spell(spell.sname, spell.slevel, spell.stype, spell.sCost, spell.sDmg))
        print(f" You have learned the {spell.sname} spell!")
        return True
    return False

  def lvl_up(self, plvl):
    print(f'You have leveled up!! You have gained {plvl} levels')
    self.player.lvl += plvl
    self.player.max_health += int((plvl*(random.randint(5,9))))
    self.player.health = self.player.max_health  
    self.player.Evasion += (plvl*int((random.randint(1,4))))
    self.player.max_mp += int((plvl*(random.randint(7,15))))
    self.player.mp = self.player.max_mp
    self.player.Accuracy += int((plvl*(random.randint(1,4))))
    self.player.strength += int((plvl*(random.randint(1,4))))
    if self.player.pclass == "Mage":
      if self.player.lvl % 2:
        self.player.addSpell("Cure")
      if self.player.lvl % 3:
        self.player.addSpell("Fireball")

    #lvl up mobs
    for bad in self.moblist:
      bad.lvl += plvl
      bad.max_health += int((plvl*(random.randint(5,8))))
      bad.health = bad.max_health
      bad.strength += int((plvl*(random.randint(1,4))))


  def Cave_Enter(self):
    clear_screen()
    self.game_hud()
    if self.BossKilled == False:
      Print_Img('Cave_Enter')
    else:
      print(" You head back to Bavaria....")
      time.sleep(1)
      ending()
    

  def Cave_tunnel(self):
    clear_screen()
    self.game_hud()
    Print_Img("Cave_tunnel")
    

  def Cave_Wall(self):
    clear_screen()
    self.game_hud()
    Print_Img("Cave_Wall")
    

  def Cave_fairy(self):
    clear_screen()
    self.game_hud()
    Print_Img("Cave_fairy")
    self.player.health = self.player.max_health
    self.player.mp = self.player.max_mp
    del self.fairys[self.fairys.index(self.position)]

    

  def Cave_Door(self):
    clear_screen()
    self.game_hud()
    found = False
    Print_Img("Cave_Door")
    #Check to see if the player has a key
    #If they do we removed it and unlock the door
    for item in self.player.inv:
      if item.iname == "Door Key":
        found = True

    if found == True:
      for item in self.player.inv:
        if item.iname == "Door Key":
          print(f" You have {item.iamount} keys")
      
      tmp = input (" Do you want to use your key to unlock the door? y/n")
      if tmp == "y":
        self.player.RemoveItem('Door Key',1)
        #We found a key so we unlock the door
        clear_screen()
        self.game_hud()
        Print_Img("Cave_Door_Unlocked")
        time.sleep(2)
        clear_screen()
        self.game_hud()
        #Show the treasure room
        Print_Img("Cave_box")
        print(' The treasure box contained')
        #Calculate the gold found
        rdmNum = random.randint(20,75)
        print(f'  {rdmNum} Gold')
        self.player.gold += rdmNum
        #Check if there was also an item found
        rdmNum = random.randint(0,10)
        if rdmNum == 8:
          rdm = random.choice(self.weapons)
          print(" You have found a new weapon")
          tmp = input(f' Do you want to equip the {rdm.wname}? y/n')
          if tmp.lower() == "y":
            print(f'  **You have equiped a {rdm.wname}**')
            self.player.addWeapon(rdm.wname, rdm.watk, rdm.w_hit, rdm.wType)
        if rdmNum == 7:
          rdm = random.choice(self.armors)
          print(f' You have found a new armor')
          tmp = input(f' Do you want to equip the {rdm.aname}? y/n')
          if tmp.lower() == "y":
            print(f'  **You have equiped a {rdm.aname}**')
            self.player.addWeapon(rdm.aname, rdm.arate, rdm.aweight, rdm.aType)
    
  def Cave_Boss(self):
    clear_screen()
    self.game_hud()
    #check to see if the boss was killed yet
    if self.BossKilled != True:
      found = False
      #Check to see if the player has a key
      #If they do we removed it and unlock the door
      for item in self.player.inv:
        if item.iname == "Skull Key":
          self.player.RemoveItem('Skull Key',1)
          found = True

      if found == True:
        #We found a key so we unlock the door
        Print_Img("Boss_Door_Unlocked")
        time.sleep(1)
        clear_screen()
        self.game_hud()
        #Enter battle with Boss
        self.BossFound = True
        self.Cave_Encounter()
      else:
        #Door is still locked
        Print_Img("Boss_Door")
    else:
      Print_Img("Boss_Killed")
      print('')
      print(' Now that you found the crown, its time to return it to the King')

  def Cave_shop(self):
    clear_screen()
    self.game_hud()
    Print_Img("Cave_shop")
    wpn = random.choice(self.weapons)
    rdn = random.randint(10,50)
    tmp=input(f'Would you like to buy a {wpn.wname} for {rdn} gold? (y/n)')
    if tmp.lower() == "y":
      if self.player.gold >= rdn:
        print(' It will serve you well!')
        self.player.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        print(f'   ****{wpn.wname} equiped****')
        self.player.gold -= rdn
      else:
        print(" You don't have enough gold")
    else:
      print('Good Bye')
    
    #remove the shop from the list
    del self.shops[self.shops.index(self.position)]
    self.Cave_tunnel()


  def Cave_Treasure(self):
    clear_screen()
    self.game_hud()
    Print_Img("Cave_box")
    if self.treasurefound != True:
      wpn = random.choice(self.weapons)
      arm = random.choice(self.armors)
      rdn = random.randint(10,50)
      print("You have found the Goblin King's treasure room")
      print(f" **** You found {wpn.wname} ****")
      print(f" **** You found {arm.aname} ****")
      print(f" **** You found {rdn} Gold ****")
      self.player.gold += rdn
      self.treasurefound = True
      #ask about equiping the stuff found
      tmp=input(f'Would you like to equipe the {wpn.wname}? (y/n)')
      if tmp.lower() == "y":
        self.player.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        print(f'   **** {wpn.wname} equiped ****')
      else:
        print(f'   **** {wpn.wname} discorded ****')
      tmp=input(f'Would you like to equipe the {arm.aname}? (y/n)')
      if tmp.lower() == "y":
        self.player.addArmor(arm.aname, arm.arate, arm.aweight, arm.aType)
        print(f'   **** {arm.aname} equiped ****')
      else:
        print(f'   **** {arm.aname} discorded ****')
    else:
      print(" You have already discoverd these treasures ")

      

  def Cave_Encounter(self):
    ready = False
    if self.BossFound != True:
      while ready != True:
        self.enemy = self.GetMonsterByID(random.randint(0,len(self.moblist)-1))
        if self.enemy.mName != 'Goblin King':
          ready = True
    else:
      self.enemy = self.GetMonsterbyName('Goblin King')

    clear_screen()
    self.game_hud()
    print('')
    if self.enemy.mobtype == 'Boss':
      print(f'you have encountered the {self.enemy.mName}')
    else:
      print(f'you have encountered a {self.enemy.mName}')
    Print_Img(self.enemy.mobtype)
    input('Press Enter to continue...')
    self.battle()

  def calc_dmg(self, pStr, pAcc=10, eEv=5, pArmor=0, pWeight=0, pwHit=10):

    cng_block = int(((5+eEv)+pArmor))
    cng_crit = int(((5+eEv)-pWeight)*0.5)
    cng_miss = int((100-pAcc)*0.2)
    cng_hit = int(((pwHit*pAcc)*0.3))
    #print(f'Block%: {cng_block}  Crit%: {cng_crit}  Miss%: {cng_miss}  hit%: {cng_hit}')
    #Build list of possiblilities
    my_list = []
    count = 0
    while (count < cng_hit):
      if count < cng_block:
        my_list.append('Blocked')
      if count < cng_crit:
        my_list.append('Crit')
      if count < cng_miss:
        my_list.append('Miss')
      my_list.append('Hit')
      count +=1
    
    #Randomly choice one
    outcome = random.choice(sorted(my_list, key=str.lower))
    if outcome == 'Blocked':
      #Our attack was blocked
      dmg = 0
    elif outcome == 'Crit':
      #Critical Hit
      dmg = random.randint(int(((pStr)*1.5)),int((pStr*2)*2.5))
    elif outcome == 'Miss':
      #Missed
      dmg = 0
    else:
      #Normal Hit
      dmg = random.randint(int(((pStr)*1)),int(((pStr)*2)))
    return dmg, outcome

  def battle(self):
    #start main battle loop
    while self.enemy.health > 0 and self.player.health > 0:
      clear_screen()
      self.game_hud()
      Print_Img(self.enemy.mobtype)

      #Clear out the variables
      Action = ""  #atk, spell, item, flee
      Spells_Found = False
      Items_found = False
      Spell_Used = "" # name of spell used
      Item_Used = "" # name of item used

      #Check to see if the player has any Spells
      if len(self.player.Spells) > 0:
        Spells_Found = True

      #Check to see if player has Potion or Ether

      for i in self.player.inv:
        if i.itype == "Heal":
          Items_found = True
          break
      
      while Action == "":
        if self.player.pclass == "Mage":
          #funtion for Mage Battle
          if Spells_Found == True and Items_found == True:
            tmp_input = input('''
            Press Enter to Attack
            Press I to use a Item
            Press S to use a Spell
            ''')
            if tmp_input.lower() == "i":
              #Item was selected
              for item in self.player.inv:
                if item.iname == "Potion":
                  tmp_answer = input("Use a Potion? y/n")
                  if tmp_answer.lower() == "y":
                    Item_Used = "Potion"
                    Action = "Item"
                elif item.iname == "Ether":
                  tmp_answer = input('Use a Ether? y/n')
                  if tmp_answer.lower() == "y":
                    Item_Used = "Ether"
                    Action = "Item"
            elif tmp_input.lower() == "s":
              #Spell was selected
              for spell in self.player.Spells:
                #Check to see if they can cast it
                if self.player.mp >= spell.sCost:
                  #Ask if they want to use item
                  tmp_answer = input(f'Use {spell.sname} Cost {spell.sCost}? y/n')
                  if tmp_answer.lower() == "y":
                    Spell_Used = spell.sname
                    Action = "Spell"
                    break
              else:
                print("You don't have enough mana to cast any spells", end='\r')
            else:
              Action = "Atk"

          
          elif Spells_Found == True and Items_found == False:
            #Spells but no items
            tmp_input = input('''
            Press Enter to Attack
            Press S to use Spell
            ''')
            if tmp_input.lower() == "s":
              #Spell was selected
              for spell in self.player.Spells:
                #Check to see if they can cast it
                if self.player.mp >= spell.sCost:
                  #Ask if they want to use item
                  tmp_answer = input(f'Use {spell.sname} Cost {spell.sCost}? y/n')
                  if tmp_answer.lower() == "y":
                    Spell_Used = spell.sname
                    Action = "Spell"
                    break
                else:
                  print("You don't have enough mana to cast any spells", end='\r')
            else:
              Action = "Atk"


          elif Spells_Found == False and Items_found == True:
            #No Spell but they have some Items
            tmp_input = input('''
            Press Enter to Attack
            Press I to use a Item
            ''')
            if tmp_input.lower() == "i":
              #Item was selected
              for item in self.player.inv:
                if item.iname == "Potion":
                  tmp_answer = input("Use a Potion? y/n")
                  if tmp_answer.lower() == "y":
                    Item_Used = "Potion"
                    Action = "Item"
                elif item.iname == "Ether":
                  tmp_answer = input('Use a Ether? y/n')
                  if tmp_answer.lower() == "y":
                    Item_Used = "Ether"
                    Action = "Item"
            else:
              Action = "Atk"
          else:
            input(" Press Enter to Attack")  
            Action = "Atk"

        elif Items_found == True:
          #Not a Mage but has Items
          tmp_input = input('''
          Press Enter to Attack
          Press I to use a Item
            ''')
          if tmp_input.lower() == "i":
            #Item was selected
            for item in self.player.inv:
              if item.iname == "Potion":
                tmp_answer = input("Use a Potion? y/n")
                if tmp_answer.lower() == "y":
                  Item_Used = "Potion"
                  Action = "Item"
              elif item.iname == "Ether":
                tmp_answer = input('Use a Ether? y/n')
                if tmp_answer.lower() == "y":
                  Item_Used = "Ether"
                  Action = "Item"
            #print("You don't have any items to use in battle")
          else:
            Action = "Atk"
        else:
          input('press Enter to attack')
          Action = "Atk"


      #Start of action code

      #players turn
      if Action == "Item":
        #Using Item
        if Item_Used == "Potion":
          self.player.RemoveItem("Potion",1)
          self.player.HealPlayer(30)
          print(' You healed for 30 hp', end='\r')
        elif Item_Used == "Ether":
          self.player.RemoveItem("Ether",1)
          self.player.RestoreMana(30)
          print('30 mana restored', end='\r')
        Action = ""
      elif Action == "Spell":
        #Using Spell
        for spells in self.player.Spells:
          if spell.sname == Spell_Used:
            self.player.mp -= spell.sCost
            if spell.sname == "Cure":
              self.player.HealPlayer(int(spell.sDmg))
              print(f' You healed for {spell.sDmg}', end='\r')
              break
            else:
              #attack with spell
              self.enemy.health -= int(spell.sDmg)
              print(f' You cast {spell.sname} for {spell.sDmg} damage', end='\r')
              break
        Action = ""
      elif Action == "Atk":
        #Attaking
        dmg, outcome = self.calc_dmg(self.player.strength, self.player.Accuracy, self.player.Evasion, self.player.Armor[0].arate, self.player.Armor[0].aweight, self.player.Weapon[0].w_hit)
        
        if outcome == "Blocked":
          #Block 
          print('                                       ', end='\r')
          print('Your attack was blocked', end='\r')
        elif outcome == "Crit":
          #Critical hit
          self.enemy.health -= int(dmg)
          print('                                           ', end='\r')
          print(f'Critical hit!! You hit {self.enemy.mName} for {int(dmg)}', end="\r")
        elif outcome == "Miss":
          #missed
          print('                                       ', end='\r')
          print('You have missed', end="\r")
        else:
          #Normal Hit
          self.enemy.health -= int(dmg)
          print('                                       ', end='\r')
          print(f'You hit the {self.enemy.mName} for {int(dmg)}', end="\r")
        Action = ""
      time.sleep(1)

      #Minion Turn
      if self.enemy.health >0:
        dmg, outcome = self.calc_dmg(self.enemy.strength)

        if outcome == "Blocked":
          #Block
          print('                                       ', end='\r')
          print(f'You blocked {self.enemy.mName}\'s Attack ', end="\r")
        elif outcome == "Crit":
          #Critical hit
          self.player.health -= int(dmg)
          print('                                          ', end='\r')
          print(f'Critical hit!! {self.enemy.mName} hit you for {int(dmg)}', end="\r")
        elif outcome == "Miss":
          #missed
          print('                                       ', end='\r')
          print(f'{self.enemy.mName} missed you', end="\r")
        else:
          #Normal Hit
          self.player.health -= int(dmg)
          print('                                       ', end='\r')
          print(f'{self.enemy.mName} hit you for {int(dmg)}', end="\r")
      time.sleep(1)

      if self.enemy.health <= 0:
        #The minion has died
        self.encounters += 1
        self.ResMonsterbyName(self.enemy.mName)

        if self.enemy.mobtype != "Boss":
          self.badKilled.append((self.position[0],self.position[1]))
          del self.badguys[self.badguys.index(self.position)]
        else:
          self.BossKilled = True
          self.BossFound = False
        #Calculate different between mod lvl and ours
        #make sure its at least 1
        if self.enemy.lvl - self.player.lvl < 1:
          upped = 1
        else:
          upped = self.enemy.lvl - self.player.lvl

        #Calculate what we gained during the battle
        gain_exp = int((random.randint(10,40)*(int(upped)))/1)
        gain_gold = int((random.randint(0,25)*(int(upped)))/1)
        self.player.exp += gain_exp
        self.player.gold += gain_gold
        
        #Check to see if item was dropped
        itemAdr = ""
        rdnNum = random.randint(0,10)
        if rdnNum > 8:
          #used to heal your player
          self.GiveItem("Potion")
          itemAdr = "Potion"
        elif rdnNum == 7:
          #used to heal your player
          self.GiveItem("Ether")
          itemAdr = "Ether"
        elif self.enemy.mName == "Goblin King":
          #used to end the game
          self.GiveItem("Kings Crown",1)
          itemAdr = "Crown"
        elif rdnNum == 2:
          #used to open doors
          self.GiveItem("Door Key")
        elif rdnNum == 5 or len(self.badguys) <= 1:
          #needed for the Boss
          Self.GiveItem("Skull Key")
   
        #print out the end of battle screen
        clear_screen()
        self.game_hud()
        print('')
        print('  Congragulations you have defeated ')
        print(f'     the {self.enemy.mName}  ')
        print('')
        print(f' Exp gained {gain_exp} ')
        print(f' Gold gained {gain_gold} ')
        print('')
        if itemAdr != "":
          print(f' {self.enemy.mName} dropped a {itemAdr}')
        print('')
        print('')
        #Check if we need to level up
        if self.player.exp // 50 >= 1:
          self.lvl_up(self.player.exp // 50)
          self.player.exp = self.player.exp % 50
        

        #return so we don't fight the monster we just revived
        input('Press Enter to continue')
        clear_screen()
        self.Cave_tunnel()
        return
        

      elif self.player.health <1:
        #you were killed
        print('You were killed!')
        time.sleep(1)
        game_over()


#Graphic Engine
def Print_Img(img_name):
  if img_name == "Cave_Enter":
    print('')
    print('You found the entrance to the cave!')
    print('')
    print('.......................................')
    print('.............________..................')
    print('.........../          \................')
    print('........../            \...............')
    print('........./              \..............')
    print('......../       __       \.............')
    print('......./       /##\       \............')
    print('....../       |####|       \...........')
    print('...../________|####|________\..........')
    print('.......................................')
    
  elif img_name == "Cave_shop":
    print('                                       ')
    print('       You found a hidden Shop         ')
    print('                                       ')
    print('.......................................')
    print('...............______..................')
    print('............\ /       \ /..............')
    print('........... /-         -\..............')
    print('...........|    _        |.............')
    print("...........|   '^'       |.............")
    print('...........| ^-{ }-8   $_|.............')
    print('...........|   ( )     _\|.............')
    print('...........|__/___\___|__|.............')
    print('.......................................')

  elif img_name == "Cave_tunnel":
    print('                                       ')
    print('       You found a new tunnel          ')
    print('                                       ')
    print('.......................................')
    print('...............______..................')
    print('............\ /       \ /..............')
    print('........... /-         -\..............')
    print('...........|             |.............')
    print('...........|             |.............')
    print('...........|             |.............')
    print('...........|             |.............')
    print('...........|_____________|.............')
    print('.......................................')

  elif img_name == "Cave_Wall":
    print('                                       ')
    print('      You have ran into a wall         ')
    print('                                       ')
    print('.......................................')
    print('...............______..................')
    print('............\ /#######\ /..............')
    print('........... /-#########-\..............')
    print('...........|#############|.............')
    print('...........|#############|.............')
    print('...........|#############|.............')
    print('...........|#############|.............')
    print('...........|#############|.............')
    print('.......................................')

  elif img_name == "King":
    print("                      +                ")
    print("                     vAv .-.           ")
    print('                     (")| # |          ')
    print("                    / v \\# | + o      ")
    print("                   c\\  //=.-'O/\"-.   ")
    print('                   |/~."|  |"-/.-\'|   ')
    print("                   / .  (__|   |  |    ")
    print("                  (=/===)`  ~-.|.-'    ")                   

  elif img_name == "Fin":
    print("              _          _                          ")
    print("             | |_ ___   | |__   ___                 ")
    print("             | __/ _ \  | '_ \ / _ \                ")
    print("             | || (_) | | |_) |  __/                ")
    print("              \__\___/  |_.__/ \___|                ")
    print("                 _   _                          _   ")
    print("   ___ ___  _ __ | |_(_)_ __  _   _  ___ ___  __| | ")
    print("  / __/ _ \| '_ \| __| | '_ \| | | |/ __/ _ \/ _` | ")
    print(" | (_| (_) | | | | |_| | | | | |_| | (_|  __/ (_| | ")
    print("  \___\___/|_| |_|\__|_|_| |_|\__,_|\___\___|\__,_| ")               

  elif img_name == "Castle":
    print("                        _              ")
    print("                       /^\             ")
    print("                       | |             ")
    print("                   _   |-|             ")
    print("            _    _/^\_ | |             ")
    print("           /^\  / [_] \+-+             ")
    print("   _      |---||-------| |_       _    ")
    print(" _/^\_    _/^\_|  [_]  |_/^\_   _/^\_  ")
    print(" |!_!|    |!_!||_______||!_!|   |!_!|  ")
    print("  | |======| |===========| |=====| |   ")
    print("  |!|      | |    /^\    | |     |!|   ")
    print("  | |      |!|   |   |   |!|     | |   ")
    print("  |_|______|_|__ |   |___|_|_____|_|   ")

    
  elif img_name == "Logo":
    print("                      ,     \    /      ,                     ")
    print("                     / \    )\__/(     / \                    ")
    print("                    /   \  (_\  /_)   /   \                   ")
    print(" __________________/_____\__\@  @/___/_____\_________________ ")
    print(" |            ____          |\../|        _                 | ")
    print(" |           |  _ \          \VV/        (_)                | ")
    print(" |           | |_) | __ ___   ____ _ _ __ _  __ _           | ")
    print(" |           |  _ < / _` \ \ / / _` | '__| |/ _` |          | ")
    print(" |           | |_) | (_| |\ V / (_| | |  | | (_| |          | ")
    print(" |           |____/ \__,_| \_/ \__,_|_|  |_|\__,_|          | ")
    print(" |__________________________________________________________| ")
    print("             |    /\ /      \\       \ /\    |                ")
    print("             |  /   V        ))       V   \  |                ")
    print("             |/     `       //        '     \|                ")
    print("             `              V                '                ")

  elif img_name == "Cave_fairy":
    print('')
    print(    'You have discovered a magical fairy')
    print('')
    print(''' **You drink from the fairy\'s fountain
        and feel refreshed**''')
    print('.......................................')
    print('...|               *              |....')
    print('...|     *                        |....')
    print('...|     ___    hey!              |....')
    print('...| * ໒(ಠ_ಠ)७    listen!         |....')
    print('...|     /-\    *                 |....')
    print('...|                    _^|^_     |....')    
    print('...|  *  _____________ |_???_|    |....')
    print('.......................................')

  elif img_name == "Cave_Door":
    print('')
    print('       You have found a door           ')
    print('     ***The door is locked***          ')
    print('.......................................')
    print('............._________.................')
    print('............|*********|................')
    print('............|*********|................')
    print('............|*********|................')
    print('............|*******0*|................')
    print('............|*********|................')
    print('............|*********|................')
    print('............|_________|................')
    print('.......................................')

  elif img_name == "Boss_Door":
      print('')
      print('   You have found a creepy door        ')
      print('     ***The door is locked***          ')
      print('.......................................')
      print('............._________.................')
      print('............|         |................')
      print('............|   ???   |................')
      print('............|  ?___?  |................')
      print('............|  / * \  |................')
      print('............|  \_µ_/  |................')
      print('............|         |................')
      print('............|_________|................')
      print('.......................................')

  elif img_name == "Boss_Door_Unlocked":
      print('')
      print('   You have found a creepy door        ')
      print(' **You use the skull key to open it**  ')
      print('.......................................')
      print('............._________.................')
      print('............|         |................')
      print('............|   ???   |................')
      print('............|  ?___?  |................')
      print('............|  / * \  |................')
      print('............|  \_µ_/  |................')
      print('............|         |................')
      print('............|_________|................')
      print('.......................................')

  elif img_name == "Boss_Killed":
    print('                                       ')
    print('                                       ')
    print('                                       ')
    print('.......................................')
    print('...............______..................')
    print('............\ /       \ /..............')
    print('........... /-         -\..............')
    print('...........|    ______   |.............')
    print('...........|   |      |  |.............')
    print('...........|_  |  &&  | _|.............')
    print('...........|@@\   __  /@@|.............')
    print('...........|@@|__|__|_|@@|.............')
    print('.......................................')

  elif img_name == "Cave_Door_Unlocked":
    print('')
    print('       You have found a door           ')
    print('  ***You use your key to open it***    ')
    print('.......................................')
    print('............._________.................')
    print('............|*********|................')
    print('............|*********|................')
    print('............|*********|................')
    print('............|*******0*|................')
    print('............|*********|................')
    print('............|*********|................')
    print('............|_________|................')
    print('.......................................')

  elif img_name == "Cave_box":
    print('')
    print('    You have found a treasure chest    ')
    print('                                       ')
    print('.......................................')
    print('..........___________________..........')
    print('......../                     \........')
    print('.......|                       |.......')
    print('.......|        _______        |.......')
    print('.......|       /       \       |.......')
    print('.......|       \_$$$$$_/       |.......')
    print('.......|       |       |       |.......')
    print('.......|       |__&&___|       |.......')
    print('........-----------------------........')
    print('.......................................')

  elif img_name == "Goblin":
    print('')
    print('.......................................')
    print(f' Lvl: {Calradia.enemy.lvl}   Name: {Calradia.enemy.mName}   ')
    print(f'       Health {Calradia.enemy.health} ')
    print('..........___________________..........')
    print('......../                     \........')
    print('.......|          , ,          |.......')
    print('.......|         (ʘдʘ)  W      |.......')
    print('.......|      d--->|<---|      |.......')
    print('.......|          |||   |      |.......')
    print('.......|          )|(          |.......')
    print('.......|        _/   \_        |.......')
    print('........-----------------------........')
    print('.......................................')

  elif img_name == "Spider":
    print('')
    print('.......................................')
    print(f' Lvl: {Calradia.enemy.lvl}   Name: {Calradia.enemy.mName}   ')
    print(f'       Health {Calradia.enemy.health} ')
    print('.......................................')
    print('.......-------------------------.......')
    print('...../                           \.....')
    print('....|                             |....')
    print('....|                             |....')
    print('....|        _ _ _ _ _ _ _        |....')
    print('....| ミ /╲/( ͜。 ͜。 ͡ʖ ͜。 ͜。)/\╱\   |....')
    print('....|   / /\              / /\ \  |....')
    print('....|_____________________________|....')
    print('.......................................')

  elif img_name == "Boss":
    print('')
    print('.......................................')
    print(f' Lvl: {Calradia.enemy.lvl}   Name: {Calradia.enemy.mName}   ')
    print(f'       Health {Calradia.enemy.health} ')
    print('                                       ')
    print('.......................................')
    print('........._____________________.........')
    print('......./           ,w,         \.......')
    print('......|           (ʘдʘ)   {#}   |......')
    print('......|      d--->(|||)<---|    |......')
    print('......|           (|||)    |    |......')
    print('......|           /   \    |    |......')
    print('......|         _/     \_       |......')
    print('.......-------------------------.......')
    print('.......................................')

  elif img_name == "Stats":
    print(f' Position {Calradia.position}')
    print('.......................................')
    print(f' Name : {Calradia.player.pname}   Class: {Calradia.player.pclass}     Lvl: {Calradia.player.lvl}')
    #If player is a mage show their MP
    if Calradia.player.pclass == "Mage":
      print(f' HP: {Calradia.player.health}/{Calradia.player.max_health}      MP: {Calradia.player.mp}/{Calradia.player.max_mp} ')
    else:
      print(f' HP: {Calradia.player.health}/{Calradia.player.max_health} ')
    print('.......................................')
    #player has a weapon equiped
    print(f' Weapon: {Calradia.player.Weapon[0].wname}   Dmg: {Calradia.player.Weapon[0].watk}')

    #Block% = (5+Evasion) - Armor Rating
    #Crit% = 100-((5 + Evasion)- Armor Weight)
    #Miss% = Player Accuracy
    #Hit% = (Weapon Hit rate * Player Accuracy)* 0.3

    cng_block = int(((5+Calradia.player.Evasion)+Calradia.player.Armor[0].arate))
    cng_crit = int(((5+Calradia.player.Evasion)-Calradia.player.Armor[0].aweight)*0.5)
    cng_miss = int(Calradia.player.Accuracy)
    cng_hit = int(((Calradia.player.Weapon[0].w_hit*Calradia.player.Accuracy)*0.3))
    print('.......................................')

    print(f' Block%: {cng_block}     Crit%: {cng_crit}   ')
    print(f" Miss%: {cng_miss}       Hit%: {cng_hit}")
    print('.......................................')
    print(f' Armor: {Calradia.player.Armor[0].aname}     Def Rating: {Calradia.player.Armor[0].arate}')
    print('.......................................')
    
    #Check for items in the Inventory
    print(" Inventory:")
    if len(Calradia.player.inv) > 0:
      for item in Calradia.player.inv:
        print(f' {item.iname}     {item.iamount}')
    else:
      print(" You don't have any items")
    print('.......................................')

    #Check for Spells
    print(" Spells:")
    if len(Calradia.player.Spells) > 0:
      for spell in Calradia.player.Spells:
        print(f' {spell.sname}     Lvl: {spell.slevel}    Dmg: {spell.sDmg}')
    else:
      print(" You don't have any Spells")
    print('.......................................')
    print('')

def Status_Screen():
#Generate options for Status Screen
  working = True
  update = True
  while working == True:
    if update == True:
      clear_screen()
      Print_Img("Stats")
      update = False
    Items_found = False
    Spells_found = False
    for item in Calradia.player.inv:
      if item.itype == "Heal":
        Items_found = True
    for spell in Calradia.player.Spells:
      if spell.sname == "Cure":
        Spells_found = True
      
    if Items_found == True and Spells_found == True:
      #player has spells and items
      tmp_input = input('''
            Press Enter to go back to the map
            Press I to use a Item
            Press S to use a Spell
            ''')
      if tmp_input.lower() == "i":
        #Item was selected
        for item in Calradia.player.inv:
          if item.iname == "Potion":
            tmp_answer = input("Use a Potion? y/n")
            if tmp_answer.lower() == "y":
              #use a potion
              Calradia.player.HealPlayer(30)
              Calradia.player.RemoveItem('Potion')
              print(' You healed for 30 hp', end='\r')
              update = True
            else:
              update = True
          elif item.iname == "Ether":
            tmp_answer = input('Use a Ether? y/n')
            if tmp_answer.lower() == "y":
              #Use a Ether
              Calradia.player.RemoveItem("Ether",1)
              Calradia.player.RestoreMana(30)
              print('30 mana restored', end='\r')
              update = True
            else:
              update = True

      elif tmp_input.lower() == "s":
        #Spell was selected
        for spell in Calradia.player.Spells:
        #Check to see if they can cast it
          if Calradia.player.mp >= spell.sCost:
          #Ask if they want to use item
            if spell.sname == "Cure":
              tmp_answer = input(f'Use {spell.sname} Cost {spell.sCost}? y/n')
              if tmp_answer.lower() == "y":
              #Use Spell
                Calradia.player.HealPlayer(int(spell.sDmg))
                print(f' You healed for {spell.sDmg}', end='\r')
                Calradia.player.mp -= spell.sCost
                update = True
              else:
                update = True
          else:
            print("You don't have enough mana to cast any spells", end='\r')
            update = True
      else:
        #exit clause
        update = False
        working = False
        break
            
    elif Spells_found == True and Items_found == False:
      #Spells but no items
      tmp_input = input('''
            Press Enter to go back to the map
            Press S to use Spell
            ''')
      if tmp_input.lower() == "s":
        #Spell was selected
        for spell in Calradia.player.Spells:
          #Check to see if they can cast it
          if Calradia.player.mp >= spell.sCost:
            #Ask if they want to use item
            if spell.sname == "Cure":
              tmp_answer = input(f'Use {spell.sname} Cost {spell.sCost}? y/n')
              if tmp_answer.lower() == "y":
              #Use Spell
                Calradia.player.HealPlayer(int(spell.sDmg))
                print(f' You healed for {spell.sDmg}', end='\r')
                Calradia.player.mp -= spell.sCost
                update = True
                break
              else:
                update = True
          else:
            print("You don't have enough mana to cast any spells", end='\r')
            update = True
      else:
        #Exit clause
        update = False
        working = False
        break

    elif Spells_found == False and Items_found == True:
      #No Spell but they have some Items
      tmp_input = input('''
      Press Enter to go back to the map
      Press I to use a Item
      ''')
      if tmp_input.lower() == "i":
      #Item was selected
        for item in Calradia.player.inv:
          if item.iname == "Potion":
            tmp_answer = input("Use a Potion? y/n")
            if tmp_answer.lower() == "y":
              #use a potion
              Calradia.player.HealPlayer(30)
              Calradia.player.RemoveItem('Potion')
              print(' You healed for 30 hp', end='\r')
              update = True
            else:
              update = True
          elif item.iname == "Ether":
            tmp_answer = input('Use a Ether? y/n')
            if tmp_answer.lower() == "y":
            #Use a Ether
              Calradia.player.RemoveItem("Ether",1)
              Calradia.player.RestoreMana(30)
              print('30 mana restored', end='\r')
              update = True
            else:
              update = True

      else:
        #Exit Clause
        update = False
        working = False
        break

    else:
      input(' Press Enter to go back to the map')
      update = False
      working = False
      break
    
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
  print("Map Complete")



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

def Debug_Menu():
  working = True
  while working == True:
    clear_screen()
    print("this is the debug menu")
    print(f"Enemey Locations {Calradia.badguys}")
    print(f"Treausre Room {Calradia.treasure}")
    print(f"Boss {Calradia.boss}")
    print(f"Shops {Calradia.shops}")
    print('')
    tmp = input("Please enter command")
    if tmp.lower() == "goto":
      tmpX = input("enter X")
      tmpY = input("enter Y")
      Calradia.position = (int(tmpX), int(tmpY))
      working = False
    elif tmp.lower() == "lvl":
      Calradia.lvl_up(1)
    elif tmp.lower() == "greed":
      Calradia.GiveItem("Door Key", 1)
      Calradia.GiveItem("Skull Key", 1)
      Calradia.GiveItem("Potion", 10)
      Calradia.GiveItem("Ether", 10)
      working = False
    else:
      working = False
    
  


#start of the game
Calradia = gameWorld()
Gen_Map()
Calradia.char_setup()
clear_screen()

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
clear_screen()
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

clear_screen()
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
    clear_screen()
    #Print_Img("Stats")
    Status_Screen()
  elif tmp.lower() == "w":
    Calradia.player.steps += 1
  #move Foward if possible
    clear_screen()
    Y+=1
  elif tmp.lower() == "a":
  #move left if possible
    Calradia.player.steps += 1
    clear_screen()
    X-=1
  elif tmp.lower() == "s":
  #move back if possible
    Calradia.player.steps += 1
    clear_screen()
    Y-=1
  elif tmp.lower() == "d":
  #move right if possible
    Calradia.player.steps += 1
    clear_screen()
    X+=1
  elif tmp.lower() == "debug":
    Debug_Menu()



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
  
