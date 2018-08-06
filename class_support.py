class Weapon:
  def __init__(self, wn, watk, whit, wType):
    self.wname = wn
    self.watk = watk
    self.w_hit = whit
    self.wType = wType

class Armor:
  def __init__(self, armn, armrate, armwg, aType):
    self.aname = armn
    self.arate = armrate
    self.aweight = armwg
    self.aType = aType

class Item:
  def __init__(self, inm, ityp, ia, iD=0):
    self.iname = inm      #name of the item
    self.itype = ityp     #type of item heal, Consumable, key
    self.iamount = ia     #You can guess what this is for
    self.iDmg = iD     #You can guess what this is for

class Spell:
  def __init__(self, sNm, slvl, sTyp, sC, sDmg):
    self.sname = sNm      #name of the Spell
    self.slevel = slvl
    self.stype = sTyp     #type of Spell: heal, Dmg
    self.sCost = sC     #mana Cost
    self.sDmg = sDmg     #Spell Dmg: For Heal this is amount
