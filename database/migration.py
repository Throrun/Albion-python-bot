
import imp
import sqlite3
######################
#BE CAREFUL THIS FUNCTION RESET ALL RECORDS

def migration():
    connection = sqlite3.connect('ITEMS.db')

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS ITEMS")
    cursor.execute("DROP TABLE IF EXISTS PROFIT")
    cursor.execute("DROP TABLE IF EXISTS BLACKMARKET")
    cursor.execute("DROP TABLE IF EXISTS CAERLEONMARKET")
    cursor.execute("DROP TABLE IF EXISTS LYMHURSTMARKET")
    cursor.execute("DROP TABLE IF EXISTS BRIDGEWATCHMARKET")
    cursor.execute("DROP TABLE IF EXISTS MARTLOCKMARKET")
    cursor.execute("DROP TABLE IF EXISTS THETFORTMARKET")
    cursor.execute("DROP TABLE IF EXISTS FORTSTERLINGMARKET")
    


    table = """CREATE TABLE ITEMS ( Name VARCHAR(50) PRIMARY KEY NOT NULL, item_picture_path VARCHAR(255) NULL); """
    #PROFIT TABLE
    cursor.execute(table)
    table = """CREATE TABLE PROFIT ( Name VARCHAR(50) NOT NULL, `5.0` FLOAT NULL, `5.1` FLOAT NULL, `5.2` FLOAT NULL, `5.3` FLOAT NULL, `6.0` FLOAT NULL, `6.1` FLOAT NULL, `6.2` FLOAT NULL, `6.3` FLOAT NULL, `7.0` FLOAT NULL, `7.1` FLOAT NULL, `7.2` FLOAT NULL, `7.3` FLOAT NULL, `8.0` FLOAT NULL, `8.1` FLOAT NULL, `8.2` FLOAT NULL, `8.3` FLOAT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)

    #BLACKMARKET
    table = """CREATE TABLE BLACKMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)
    
    #CAERLEONMARKET
    table = """CREATE TABLE CAERLEONMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)

    #LYMHURSTMARKET
    table = """CREATE TABLE LYMHURSTMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)
    
    #BRIDGEWATCHMARKET
    table = """CREATE TABLE BRIDGEWATCHMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)
    
    #MARTLOCKMARKET
    table = """CREATE TABLE MARTLOCKMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)
    
    #THETFORTMARKET
    table = """CREATE TABLE THETFORTMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)
    
    #FORTSTERLINGMARKET
    table = """CREATE TABLE FORTSTERLINGMARKET ( Name VARCHAR(50) NOT NULL, `5.0` INT NULL, `5.1` INT NULL, `5.2` INT NULL, `5.3` INT NULL, `6.0` INT NULL, `6.1` INT NULL, `6.2` INT NULL, `6.3` INT NULL, `7.0` INT NULL, `7.1` INT NULL, `7.2` INT NULL, `7.3` INT NULL, `8.0` INT NULL, `8.1` INT NULL, `8.2` INT NULL, `8.3` INT NULL, FOREIGN KEY (Name) REFERENCES ITEMS(Name), UNIQUE (Name) )"""
    cursor.execute(table)    
    #TODO ADD TABLE FOR CITY x6

    print("table items created")
    
    ####DEFAULT ITEMS
    
    file = open("database\Clothes.txt")
    
    for item in file:
        
        query = """INSERT INTO `ITEMS` (`Name`, `item_picture_path`) VALUES (?, ?);"""
        items = (item, 'NULL')
        cursor.execute(query, items)
        
        query = """INSERT INTO `PROFIT` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        cursor.execute(query, items)
        
        query = """INSERT INTO `BLACKMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        cursor.execute(query, items)
        
        query = """INSERT INTO `CAERLEONMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        cursor.execute(query, items)
        
        query = """INSERT INTO `LYMHURSTMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        
        cursor.execute(query, items)
        query = """INSERT INTO `BRIDGEWATCHMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        
        cursor.execute(query, items)
        query = """INSERT INTO `MARTLOCKMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        
        cursor.execute(query, items)
        query = """INSERT INTO `THETFORTMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        cursor.execute(query, items)
        
        query = """INSERT INTO `FORTSTERLINGMARKET` (`Name`, `5.0`, `5.1`, `5.2`, `5.3`, `6.0`, `6.1`, `6.2`, `6.3`, `7.0`, `7.1`, `7.2`, `7.3`, `8.0`, `8.1`, `8.2`, `8.3`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        items = (item, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
        cursor.execute(query, items)
    connection.commit()
    connection.close()

def showAll():
    connection = sqlite3.connect('Test.db')

    cursor = connection.cursor()
    #cursor.execute("SELECT * FROM ITEMS")
    

    connection.close()