import random
import time
import class_player
import class_support
import class_monster
import helper_functions
import class_graphics

def game_over():
  options = ["Death One","Death Two", "Death Three", "Death Four", "Death Five", "Death Six", "Death Seven"]
  helper_functions.clear_screen()
  self.graphics.CallArtByName(random.choice(options)).ShowArt()
  print("")
  print("")
  print("Press Enter to try again")

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
    self.graphics = class_graphics.Graphics_Engine() 
    #self.graphics.InitImages()

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
      helper_functions.clear_screen()
      self.graphics.CallArtByName("Logo").ShowArt()
      self.player.pname=input('Please enter your name')
      helper_functions.clear_screen()
      self.graphics.CallArtByName("Class Selection").ShowArt()
      print('')
      print('Selection: ')
      print('')
      tmp = input('')

      if tmp == "1":
        #Figher class
        helper_functions.clear_screen()
        self.player.strength=random.randint(8,13)
        self.player.pclass = "Fighter"
        weapon = "Short Sword"
        armor = "Cloth Armor"
        health = 35
        Ev = 8
        Acc = 45
      elif tmp == "2":
        #Monk Class
        helper_functions.clear_screen()
        self.player.strength=random.randint(7,10)
        self.player.pclass = "Monk"
        weapon = "Brass Knuckles"
        armor = "Shirt"
        health = 25
        Ev = 12
        Acc = 35
      elif tmp == "3":
        #Thief Class
        helper_functions.clear_screen()
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
      helper_functions.clear_screen()
      print("")
      print(f'You chose :')
      print("")
      print(f"Name: {self.player.pname}")
      print(f"Class: {self.player.pclass}")
      print(f"Health: {self.player.health}/{self.player.max_health}")
      if self.player.pclass == "Mage":
        print(f"Mana: {self.player.mp}/{self.player.max_mp}")
      print(f"Evasion: {self.player.Evasion}   Accuracy: {self.player.Accuracy}")
      print(f"Strength: {self.player.strength} ")
      print(f"Weapon: {self.player.Weapon[0].wname}  Atk rate: {self.player.Weapon[0].watk}")
      print(f"Armor: {self.player.Armor[0].aname}  Def rate: {self.player.Armor[0].arate}")
      print(' ')
      if self.player.pclass == "Fighter":
        self.graphics.CallArtByName("Fighter").ShowArt()
        #class_oldgraphic.Print_Img("Fighter")
      elif self.player.pclass == "Monk":
        self.graphics.CallArtByName("Monk").ShowArt()
        #class_oldgraphic.Print_Img("Monk")
      elif self.player.pclass == "Thief":
        self.graphics.CallArtByName("Thief").ShowArt()
        #class_oldgraphic.Print_Img("Thief")
      elif self.player.pclass == "Mage":
        self.graphics.CallArtByName("Mage").ShowArt()
        #class_oldgraphic.Print_Img("Mage")
      print("")
      tmp = input("Do you want to keep this Character? y/n")
      if tmp.lower() != "n":
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
        self.addSpell("Cure")
      if self.player.lvl % 3:
        self.addSpell("Fireball")

    #lvl up mobs
    for bad in self.moblist:
      bad.lvl += plvl
      bad.max_health += int((plvl*(random.randint(5,8))))
      bad.health = bad.max_health
      bad.strength += int((plvl*(random.randint(1,4))))


  def Cave_Enter(self):
    helper_functions.clear_screen()
    self.game_hud()
    if self.BossKilled == False:
      self.graphics.CallArtByName("Cave_Enter").ShowArt()
    else:
      print(" You head back to Bavaria....")
      time.sleep(1)
      ending()
    
  def Cave_tunnel(self):
    helper_functions.clear_screen()
    self.game_hud()
    self.graphics.CallArtByName("Cave_tunnel").ShowArt()
    

  def Cave_Wall(self):
    helper_functions.clear_screen()
    self.game_hud()
    self.graphics.CallArtByName("Cave_Wall").ShowArt()
    

  def Cave_fairy(self):
    helper_functions.clear_screen()
    self.game_hud()
    self.graphics.CallArtByName("Cave_fairy").ShowArt()
    self.player.health = self.player.max_health
    self.player.mp = self.player.max_mp
    del self.fairys[self.fairys.index(self.position)]
    
  def Cave_Door(self):
    helper_functions.clear_screen()
    self.game_hud()
    found = False
    self.graphics.CallArtByName("Cave_Door").ShowArt()
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
        helper_functions.clear_screen()
        self.game_hud()
        self.graphics.CallArtByName("Cave_Door_unlocked").ShowArt()
        time.sleep(2)
        helper_functions.clear_screen()
        self.game_hud()
        #Show the treasure room
        self.graphics.CallArtByName("Cave_box").ShowArt()
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
    helper_functions.clear_screen()
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
        self.graphics.CallArtByName("Boss_Door_Unlocked").ShowArt()
        time.sleep(1)
        helper_functions.clear_screen()
        self.game_hud()
        #Enter battle with Boss
        self.BossFound = True
        self.Cave_Encounter()
      else:
        #Door is still locked
        self.graphics.CallArtByName("Boss_Door").ShowArt()
    else:
      self.graphics.CallArtByName("Boss_Killed").ShowArt()
      print('')
      print(' Now that you found the crown, its time to return it to the King')

  def Cave_shop(self):
    helper_functions.clear_screen()
    self.game_hud()
    self.graphics.CallArtByName("Cave_shop").ShowArt()
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
    helper_functions.clear_screen()
    self.game_hud()
    self.graphics.CallArtByName("Cave_box").ShowArt()
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
        self.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        print(f'   **** {wpn.wname} equiped ****')
      else:
        print(f'   **** {wpn.wname} discorded ****')
      tmp=input(f'Would you like to equipe the {arm.aname}? (y/n)')
      if tmp.lower() == "y":
        self.addArmor(arm.aname, arm.arate, arm.aweight, arm.aType)
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

    helper_functions.clear_screen()
    self.game_hud()
    print('')
    if self.enemy.mobtype == 'Boss':
      print(f'you have encountered the {self.enemy.mName}')
    else:
      print(f'you have encountered a {self.enemy.mName}')
    self.graphics.CallArtByName("self.enemy.mobtype").ShowArt()
    input('Press Enter to continue...')
    self.battle()

  def Debug_Menu(self):
    working = True
    while working == True:
      helper_functions.clear_screen()
      print("this is the debug menu")
      print(f"Enemey Locations {self.badguys}")
      print(f"Treausre Room {self.treasure}")
      print(f"Boss {self.boss}")
      print(f"Shops {self.shops}")
      print('')
      tmp = input("Please enter command")
      if tmp.lower() == "goto":
        tmpX = input("enter X")
        tmpY = input("enter Y")
        self.position = (int(tmpX), int(tmpY))
        working = False
      elif tmp.lower() == "lvl":
        self.lvl_up(1)
      elif tmp.lower() == "greed":
        self.GiveItem("Door Key", 1)
        self.GiveItem("Skull Key", 1)
        self.GiveItem("Potion", 10)
        self.GiveItem("Ether", 10)
        working = False
      else:
        working = False
        
  def Status_Screen(self):
  #Generate options for Status Screen
    working = True
    update = True
    while working == True:
      if update == True:
        helper_functions.clear_screen()
        self.Stats()
        update = False
      Items_found = False
      Spells_found = False
      
      for item in self.player.inv:
        if item.itype == "Heal":
          Items_found = True
      for spell in self.player.Spells:
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
          for item in self.player.inv:
            if item.iname == "Potion":
              tmp_answer = input("Use a Potion? y/n")
              if tmp_answer.lower() == "y":
              #use a potion
                self.player.HealPlayer(30)
                self.player.RemoveItem('Potion')
                print(' You healed for 30 hp', end='\r')
                update = True
              else:
                update = True
            elif item.iname == "Ether":
              tmp_answer = input('Use a Ether? y/n')
              if tmp_answer.lower() == "y":
                #Use a Ether
                self.player.RemoveItem("Ether",1)
                self.player.RestoreMana(30)
                print('30 mana restored', end='\r')
                update = True
              else:
                update = True
        elif tmp_input.lower() == "s":
          #Spell was selected
          for spell in self.player.Spells:
          #Check to see if they can cast it
            if self.player.mp >= spell.sCost:
            #Ask if they want to use item
              if spell.sname == "Cure":
                tmp_answer = input(f'Use {spell.sname} Cost {spell.sCost}? y/n')
                if tmp_answer.lower() == "y":
                  #Use Spell
                  self.player.HealPlayer(int(spell.sDmg))
                  print(f' You healed for {spell.sDmg}', end='\r')
                  self.player.mp -= spell.sCost
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
          for spell in self.player.Spells:
            #Check to see if they can cast it
            if self.player.mp >= spell.sCost:
              #Ask if they want to use item
              if spell.sname == "Cure":
                tmp_answer = input(f'Use {spell.sname} Cost {spell.sCost}? y/n')
                if tmp_answer.lower() == "y":
                #Use Spell
                  self.player.HealPlayer(int(spell.sDmg))
                  print(f' You healed for {spell.sDmg}', end='\r')
                  self.player.mp -= spell.sCost
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
          for item in self.player.inv:
            if item.iname == "Potion":
             tmp_answer = input("Use a Potion? y/n")
             if tmp_answer.lower() == "y":
               #use a potion
               self.player.HealPlayer(30)
               self.player.RemoveItem('Potion')
               print(' You healed for 30 hp', end='\r')
               update = True
             else:
               update = True
            elif item.iname == "Ether":
             tmp_answer = input('Use a Ether? y/n')
            if tmp_answer.lower() == "y":
              #Use a Ether
                self.player.RemoveItem("Ether",1)
                self.player.RestoreMana(30)
                print('30 mana restored', end='\r')
                update = True
            else:
                update = True
         #Exit Clause
          update = False
          working = False
          break
      else:
        input(' Press Enter to go back to the map')
        update = False
        working = False
        break

  def Stats(self):
    print(f' Position {self.position}')
    print('.......................................')
    print(f' Name : {self.player.pname}   Class: {self.player.pclass}     Lvl: {self.player.lvl}')
    #If player is a mage show their MP
    if self.player.pclass == "Mage":
      print(f' HP: {self.player.health}/{self.player.max_health}      MP: {self.player.mp}/{self.player.max_mp} ')
    else:
      print(f' HP: {self.player.health}/{self.player.max_health} ')
    print('.......................................')
    #player has a weapon equiped
    print(f' Weapon: {self.player.Weapon[0].wname}   Dmg: {self.player.Weapon[0].watk}')

    #Block% = (5+Evasion) - Armor Rating
    #Crit% = 100-((5 + Evasion)- Armor Weight)
    #Miss% = Player Accuracy
    #Hit% = (Weapon Hit rate * Player Accuracy)* 0.3

    cng_block = int(((5+self.player.Evasion)+self.player.Armor[0].arate))
    cng_crit = int(((5+self.player.Evasion)-self.player.Armor[0].aweight)*0.5)
    cng_miss = int(self.player.Accuracy)
    cng_hit = int(((self.player.Weapon[0].w_hit*self.player.Accuracy)*0.3))
    print('.......................................')

    print(f' Block%: {cng_block}     Crit%: {cng_crit}   ')
    print(f" Miss%: {cng_miss}       Hit%: {cng_hit}")
    print('.......................................')
    print(f' Armor: {self.player.Armor[0].aname}     Def Rating: {self.player.Armor[0].arate}')
    print('.......................................')
    #Check for items in the Inventory
    print(" Inventory:")
    if len(self.player.inv) > 0:
      for item in self.player.inv:
        print(f' {item.iname}     {item.iamount}')
    else:
      print(" You don't have any items")
    print('.......................................')

    #Check for Spells
    print(" Spells:")
    if len(self.player.Spells) > 0:
      for spell in self.player.Spells:
        print(f' {spell.sname}     Lvl: {spell.slevel}    Dmg: {spell.sDmg}')
    else:
      print(" You don't have any Spells")
    print('.......................................')
    print('')

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
      helper_functions.clear_screen()
      self.game_hud()
      self.graphics.CallArtByName(self.enemy.mobtype).ShowArt()

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
          self.GiveItem("Skull Key")
   
        #print out the end of battle screen
        helper_functions.clear_screen()
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
        helper_functions.clear_screen()
        self.Cave_tunnel()
        return
        

      elif self.player.health <1:
        #you were killed
        print('You were killed!')
        time.sleep(1)
        game_over()
