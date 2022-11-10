import pyautogui
from fixtures import findEnchant, legitClick, findTier, lookAtPrice


class Item:
   name = ''
   tier = 5
   enchant = 0
   imgPath = ''
   price = 0
   city = 'BLACKMARKET'
    
   def __init__(self, name, tier=6, ench=0, city='CAERLEONMARKET', tax=False):
      self.name = name
      self.tier = tier
      self.enchant = ench
      self.city = city
      self.tax = tax

   #TODO
   
   def goToItem(self):
      #TODO CHECK if shop is open
      legitClick(530, 260)
      pyautogui.write(self.name, 0.05)
      legitClick(1150, 420)
      legitClick(1120, 320)
    #getformDB
    #export2DB
   
   #first you have to use goToItem
   def checkSingleItemPrice(self):
      #TODO CHECK goToItem was worked
      legitClick(400, 390)#open tier dropdown
      legitClick(*findTier(self.tier))
      legitClick(520,390)#open enchant dropdown
      legitClick(*findEnchant(self.enchant))
      self.price = lookAtPrice()
   
   def CheckTier(self):
      legitClick(400, 390)#open tier dropdown
      legitClick(*findTier(self.tier))
   
   def CheckEnchant(self):
      legitClick(520,390)#open enchant dropdown
      legitClick(*findEnchant(self.enchant))
      self.price = lookAtPrice()
   
   
   @staticmethod
   def closeWindow():
      legitClick(820, 300)
      
   def getPrice(self):
      return self.price
   
   