import class_support

class player:
  def __init__(self):
    self.pname = ""
    self.pclass = ""
    self.lvl = 1
    self.health = 25
    self.max_health = 25
    self.mp = 0
    self.max_mp = 0
    self.exp = 0
    self.Evasion = 5
    self.Accuracy = 5
    self.HitPer = 0
    self.strength = 5
    self.gold = 0
    self.steps = 0
    self.Armor = []
    self.Weapon = []
    self.Spells = []
    self.inv = []

  def char_setup(self):
    finished = False
    while finished == False:
      #Setup Character
      clear_screen()
      self.pname=input('Please enter your name')
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
        self.strength=random.randint(8,13)
        self.pclass = "Fighter"
        weapon = "Short Sword"
        armor = "Cloth Armor"
        health = 35
        Ev = 8
        Acc = 45
      elif tmp == "2":
        #Monk Class
        clear_screen()
        self.strength=random.randint(7,10)
        self.pclass = "Monk"
        weapon = "Brass Knuckles"
        armor = "Shirt"
        health = 25
        Ev = 12
        Acc = 35
      elif tmp == "3":
        #Thief Class
        clear_screen()
        self.pclass = "Thief"
        weapon = "Small Knife"
        armor = "Lether Armor"
        health = 15
        Ev = 20
        Acc = 30
        self.strength=random.randint(5,8)
      elif tmp == "4":
        #Mage Class
        self.pclass = "Mage"
        health = 15
        Ev = 12
        Acc = 20
        weapon = "Wooden Staff"
        armor = "Robe"
        self.max_mp = 30
        self.mp = self.max_mp
        self.strength=random.randint(4,6)
      else:
        #User didn't choice a class so we will assign open
        #They get a Loser Class
        print("""
        Guess you didn't want to choice a class. 
        Well i will choice for you slacker!
        """)
        self.pclass = "Loser"
        self.strength = random.randint(1,3)
        weapon = "Stick"
        armor = "Cover-all"
        health = 10
        Ev = 5
        Acc = 5
      #Display to the user what they choose
      if self.pname != "GOD":
        self.health = health
        self.max_health = health
        self.Evasion = Ev
        self.Accuracy = Acc
        for item in Calradia.weapons:
            if item.wname == weapon:
              wpn = item
        self.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        for item in Calradia.armors:
            if item.aname == armor:
              amn = item
        self.addArmor(amn.aname,amn.arate,amn.aweight, amn.aType)
        self.inv.clear()
      else:
        self.addItem("Door Key", 1)
        self.addItem("Skull Key", 1)
        self.addItem("Potion", 10)
        self.addItem("Ether", 10)
        self.addSpell("Cure")
        self.addSpell("Fireball")
        self.health = 60
        self.max_health = self.health
        self.Evasion = 40
        self.Accuracy = 40
        self.strength = 25
        for item in Calradia.weapons:
            if item.wname == weapon:
              wpn = item
        self.addWeapon(wpn.wname, wpn.watk, wpn.w_hit, wpn.wType)
        for item in Calradia.armors:
            if item.aname == armor:
              amn = item
        self.addArmor(amn.aname,amn.arate,amn.aweight, amn.aType)
      clear_screen()
      print("")
      print(f'You choose :')
      print(f"Name: {self.pname}")
      print(f"Class: {self.pclass}")
      print(f"Health: {self.health}/{self.max_health}")
      if Calradia.player.pclass == "Mage":
        print(f"Mana: {self.mp}/{self.max_mp}")
      print(f"Evasion: {self.Evasion}   Accuracy: {self.Accuracy}")
      print(f"Strength: {self.strength} ")
      print(f"Weapon: {self.Weapon[0].wname}  Atk rate: {self.Weapon[0].watk}")
      print(f"Armor: {self.Armor[0].aname}  Def rate: {self.Armor[0].arate}")
      tmp = input("Do you want to reroll your Character? y/n")
      if tmp.lower() != "y":
        finished = True
      

  def addItem(self, iname, iAmount=1):
    #Check to see if player already has the Item
    for item in self.inv:
      if item.iname == iname:
        if item.itype != "Key":
          #Update Amount
          item.iamount += iAmount
          return True
    #couldn't find the item so we are going to add it
    for item in Calradia.items:
      if item.iname == iname:
        self.inv.append(Item(item.iname, item.itype, iAmount, item.iDmg))
        return True

  def RemoveItem(self, pn, pA=1):
    #Remove an item from our inventory
    for i in self.inv:
      if i.iname == pn:
        if i.iamount > pA:
          i.iamount -= pA
        else:
          del self.inv[self.GetItemIDbyName(pn)]
        return True
    return False

  def GetItemIDbyName(self, pn):
    for x,m in enumerate(self.inv):
      if m.iname == pn:
        return x
    return -1

  def addWeapon(self, wn, watk, whit, wType):
    #add an Weapons to our slot
    if len(self.Weapon) > 0:
      self.Weapon[0].wname = wn
      self.Weapon[0].watk = watk
      self.Weapon[0].w_hit = whit
      self.Weapon[0].wType = wType
      return True
    else:
      self.Weapon.append(Weapon(wn, watk, whit, wType))
      return True

  def addArmor(self, armN, armRate, armwg, armType):
    #add Armor to our slot
    if len(self.Armor) > 0:
      self.Armor[0].aname = armN
      self.Armor[0].arate = armRate
      self.Armor[0].aweight = armwg
      self.Armor[0].aType = armType
      return True
    else:
      self.Armor.append(Armor(armN, armRate, armwg, armType))
      return True

  def addSpell(self, sname):
    #Check to see if player already has the Spell
    for spell in self.Spells:
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
    for spell in Calradia.Spells:
      if spell.sname == sname:
        self.Spells.append(Spell(spell.sname, spell.slevel, spell.stype, spell.sCost, spell.sDmg))
        print(f" You have learned the {spell.sname} spell!")
        return True
    return False
     
  def HealPlayer(self, Amount):
    #Use a Potion/Heal spell
    self.health += Amount
    if self.health > self.max_health:
      self.health = self.max_health
      return False
    return True

  def RestoreMana(self, Amount):
    #Use a Ether
    self.mp += Amount
    if self.mp > self.max_mp:
      self.mp = self.max_mp
      return False
    return True
