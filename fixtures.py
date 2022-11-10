from hashlib import blake2b
from PIL import Image
import pyautogui as auto
import cv2 as cv
import numpy as np
import time as t
import pytesseract



def legitClick(x, y, d=0.1):
    auto.moveTo(x, y, d)
    auto.mouseDown()
    auto.mouseUp()
    
def clearstring(string):
    result = ""
    for number in string:
        if(ord(number)>=48 and ord(number)<=57):
            result += number
    return result

###TODO
"""def WaitUntilResult(result,time):
    while time:
        if result == '' or result == None:
            t.sleep(0.5)
            time-=0.5
        else:
            return result
    exit("WaitUntilResult time out")"""

def riseUpContrast(picture):
    img = cv.imread(picture)
    lab =  cv.cvtColor(img,cv.COLOR_BGR2LAB)
    l_channel, a, b = cv.split(lab)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l_channel)
    limg = cv.merge((cl,a,b))     
    enchanced_img = cv.cvtColor(limg, cv.COLOR_LAB2LBGR)
    #result = np.hstack((img, enchanced_img))
    grey = cv.cvtColor(enchanced_img,cv.COLOR_BGR2GRAY)
    thresh, image_black = cv.threshold(enchanced_img, 130, 255, cv.THRESH_BINARY)
    #cv.imshow("siema",image_black)
    #cv.waitKey()
    return grey

def findTier(Tier):
    i=0
    while i < 5:
        t.sleep(i*0.05)    
        loc = auto.locateOnScreen("resources\\tier_8.png", confidence=0.8)
        if loc==None:
            i +=1
        else:
            loc = auto.center(loc)
            result = loc[0],loc[1] + 26*(Tier-8) 
            return result
    exit("Can't locate Tier")

def lookAtPrice():
    i=0
    while i < 5:
        t.sleep(i*0.05)
        auto.screenshot('screenshot.png',region=(895, 355, 85, 20))      
        img = riseUpContrast('screenshot.png')
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        number = pytesseract.image_to_string(img)
        
        if clearstring(number).isdigit():
            result = clearstring(number)
            break
        elif number == "E IS CURRENTL'":
            result = -1
            break
        else:
            i += 1
            result = 0
            
    return result #if result is -1 sell order doesn't exist

def findEnchant(ench):
    loc = (560,422+26*ench)
    return loc