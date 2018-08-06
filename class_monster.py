class monster:
    def __init__(self,pn, plvl, php_top, ps_top, pTyp):
      self.lvl = plvl
      self.health = random.randint(2, php_top)
      self.max_health = self.health
      self.strength = random.randint(2,ps_top)
      self.mName = pn
      self.mobtype = pTyp
