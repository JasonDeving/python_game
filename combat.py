import random

class Combat:
  dodge_limit = 6
  attack_limit = 6
  
  def dodge(self):
    roll = random.randint(1, self.dodge_limit)
    return roll > 4
  
  def attack(self):
    roll = random.randint(1, self.attack_limit)
    return roll > 4
  
  # from monster import Goblin
  # hoggle = Goblin()
  # hoggle.attack()
  # hoggle.dodge()
  # from character import Character
  # player = Character()
  # Jason
  # S
  # player.attack()