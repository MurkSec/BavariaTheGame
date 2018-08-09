import class_support
import random

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

  # Give the player an item.
  # Expects a parameter of type item from class_support.py
  # Returns True.
  def GiveItem(self, pItem, pAmount=1):
    for item in self.inv:
      if item.iname == pItem.iname:
        item.iamount += pAmount
        return True
    self.inv.append(pItem)
    return True

  #Deprecated, we now pass the item as a parameter
  #def GiveItem(self, iname, iAmount=1):
    #Check to see if player already has the Item
  #  for item in self.inv:
  #    if item.iname == iname:
  #      if item.itype != "Key":
          #Update Amount
  #        item.iamount += iAmount
  #        return True
  #  return False
    #couldn't find the item so we are going to add it
    #for item in self.items:
    #  if item.iname == iname:
    #    self.inv.append(class_support.Item(item.iname, item.itype, iAmount, item.iDmg))
    #    return True    
 
  def RemoveItem(self, pItemName, pAmount=1):
    #Remove an item from our inventory
    for i in self.inv:
      if i.iname == pItemName:
        if i.iamount > pAmount:
          i.iamount -= pAmount
        else:
          del self.inv[self.GetItemIDbyName(pItemName)]
        return True
    return False

  def GetItemIDbyName(self, pn):
    for x,m in enumerate(self.inv):
      if m.iname == pn:
        return x
    return -1

  # Returns the item object by parameter input of the item name.
  def GetItemByName(self, pItemName):
    for i in self.inv:
      if i.iname == pItemName:
        return i
      else:
        return False

  def addArmor(self, armN, armRate, armwg, armType):
    #add Armor to our slot
    if len(self.Armor) > 0:
      self.Armor[0].aname = armN
      self.Armor[0].arate = armRate
      self.Armor[0].aweight = armwg
      self.Armor[0].aType = armType
      return True
    else:
      self.Armor.append(class_support.Armor(armN, armRate, armwg, armType))
      return True

  def addWeapon(self, wn, watk, whit, wType):
    #add an Weapons to our slot
    if len(self.Weapon) > 0:
      self.Weapon[0].wname = wn
      self.Weapon[0].watk = watk
      self.Weapon[0].w_hit = whit
      self.Weapon[0].wType = wType
      return True
    else:
      self.Weapon.append(class_support.Weapon(wn, watk, whit, wType))
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
    for spell in self.Spells:
      if spell.sname == sname:
        self.Spells.append(class_support.Spell(spell.sname, spell.slevel, spell.stype, spell.sCost, spell.sDmg))
        print(f" You have learned the {spell.sname} spell!")
        return True
    return False