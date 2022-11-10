import pyautogui as auto
from fileinput import filelineno
from os import remove
from pickle import FALSE
from database.migration import migration, showAll
from database.database import Calculate, Export2DB, ImportFromDB, ShowProfit
from Item import Item
import time

from fixtures import legitClick, lookAtPrice, riseUpContrast

file = open('itemlist2.txt')
i=3
"""
while i:
    time.sleep(1)
    print (i)
    i-=1"""
itemasas = []
for item in file:
    item = item.removesuffix("\n")
    itemasas.append(item)
        
def checkFromListBM():
    
    for items in itemasas:
        j=6
        
        while j<=7:
            i=0
            Item(items).goToItem()
            Item(items,j,i,'BLACKMARKET').CheckTier()
            while(i<=1):
                item = Item(items, j, i,'BLACKMARKET', True)
                item.CheckEnchant()
                Export2DB(item.price,item.name,item.tier,item.enchant,item.city, item.tax)
                print(ImportFromDB(item.name,item.tier,item.enchant,item.city))
                i+=1
                del item
            Item.closeWindow()
            j+=1
def checkFromListCM():
    for items in itemasas:
        j=6
        while j<=7:
            i=0
            Item(items).goToItem()
            Item(items,j,i,'CAERLEONMARKET').CheckTier()
            while(i<=1):
                item = Item(items, j, i,'CAERLEONMARKET', False)
                item.CheckEnchant()
                Export2DB(item.price,item.name,item.tier,item.enchant,item.city, item.tax)
                print(ImportFromDB(item.name,item.tier,item.enchant,item.city))
                i+=1
                del item
            Item.closeWindow()
            j+=1
def result():
    Calculate('CAERLEONMARKET')
    i=5
    while i<=8:
        j=0
        while j<=3:
            siema = ShowProfit(0.10,i,j)
            if siema:
                print (siema[0][1])
                for x in siema:
                    name = str(x[0])
                    name = name.removesuffix("\n")
                    price = ImportFromDB(name, i, j,"CAERLEONMARKET")
                    print(name + ' - ' + str(int(x[2]*100)) + '% - ' + str(price) +'\n\n' )
            j+=1
        i+=1

def sell(amount=48):
    while amount:
        legitClick(1150, 420)
        legitClick(1125, 320)
        legitClick(450, 620)
        legitClick(770, 710)
        time.sleep(0.2)
        amount-=1
    
def locate():
    while True:
        print(auto.position())
        
#migration()
#checkFromListCM()    
#checkFromListBM()
#result()
#sell(3)