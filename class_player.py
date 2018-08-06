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
