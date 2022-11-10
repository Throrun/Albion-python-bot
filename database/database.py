import re
import sqlite3
import math

def Export2DB(price,item,tier,enchant,Nametable,tax):
    connection = sqlite3.connect('ITEMS.db')

    cursor = connection.cursor()
    
    if tax:
        price = int(price)*0.895
        price = math.trunc(price)
        print("murzyn")
    
    query = f"""UPDATE `{Nametable}` SET `{tier}.{enchant}` = {price} WHERE `Name` = '{item}\n';"""
    cursor.execute(query)
    connection.commit()
    connection.close()
    
    
def ImportFromDB(item,tier,enchant,Nametable):
    connection = sqlite3.connect('ITEMS.db')

    cursor = connection.cursor()
    query = f"""SELECT `{tier}.{enchant}` FROM `{Nametable}` WHERE `Name` = '{item}\n' ;"""
    cursor.execute(query)
    result = cursor.fetchone()#TO DO PROBLEM WITH TOUPLE
    if result!=None:
        result = result[0]
    connection.close()
    return result

def Calculate(city):
    file = open("database\Clothes.txt")
    items = []
    for item in file:
        item = item.removesuffix("\n")
        items.append(item)
        
    for item in items:
        tier = 5
        while(tier<=8):
            enchant = 0
            while(enchant<=3):
                BMprice = ImportFromDB(item,tier,enchant,'BLACKMARKET')
                cityprice = ImportFromDB(item,tier,enchant,city)
                print(str(item) + " " + str(tier) + " " + str(enchant))
                if(BMprice == 'NULL' or cityprice == 'NULL' or BMprice == None or cityprice == None):
                    result='NULL'
                else:
                    result = (BMprice-cityprice)/(cityprice-1)
                    Export2DB((round(result,2)),item,tier,enchant,"PROFIT", False)
                
                enchant +=1
            tier +=1
    

def ShowProfit(percent,tier,enchant):
    connection = sqlite3.connect('ITEMS.db')

    cursor = connection.cursor()
    
    #query= f"""SELECT `Name`, `{tier}.{enchant}` FROM PROFIT WHERE """
    query = f"""SELECT Name,
    CASE WHEN "{tier}.{enchant}" > {percent} THEN '{tier}.{enchant}' END AS Tier,
    "{tier}.{enchant}" AS PROFIT
  FROM PROFIT
 WHERE "{tier}.{enchant}" > {percent} AND "{tier}.{enchant}" <> 'NULL' ;

"""
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        result = 0
    connection.close()
    return result
