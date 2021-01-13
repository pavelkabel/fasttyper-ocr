import numpy as nm  
import pytesseract 
import pyautogui
from pyautogui import *
from PIL import ImageGrab 
import keyboard
import pynput
import time
import random
from pynput.keyboard import Controller
keyboard1 = Controller()

global delay
#ui
userWantSpeed = input("Do you want to change speed? y/n:")
if userWantSpeed == "y":
    delay = input("enter time interval between keystrokes (in seconds):")
    time.sleep(3)
else:
    delay = 0
    time.sleep(3)


def fastKeyboard(string):
    #optimize text recieved by tesseract
    stringSpaced = string.ljust(len(string) + 1)
    if string.count(' ') <= 3:
        stringProcessed = " ".join(string.replace(" ",""))
        print(stringProcessed)
    else:
        stringProcessed = string

    stringSpaced = stringProcessed.ljust(len(stringProcessed) + 1)
    for character in stringSpaced:  
        keyboard1.type(character)  
        time.sleep(float(delay)) 

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@run_once
def imgToString(): 
    pytesseract.pytesseract.tesseract_cmd =r'C:\\Users\\Public\\Tesseract-OCR\\tesseract.exe'
    while(True): 
        #configure screen area
        cap = ImageGrab.grab(bbox =(0, 220, 1650, 285)) 
        #here you can configure language
        tesstr = pytesseract.image_to_string(cap, lang ='eng') 
        print(tesstr.rsplit("\n",1)[0])
        fastKeyboard(tesstr.rsplit("\n",1)[0])
        time.sleep(0.5)
        checkNextLine()
       
def imgToString2(): 
    pytesseract.pytesseract.tesseract_cmd =r'C:\\Users\\Public\\Tesseract-OCR\\tesseract.exe'
    while(True): 
        #configure screen area
        cap = ImageGrab.grab(bbox =(0, 220, 1650, 285)) 
         #here you can configure language
        tesstr = pytesseract.image_to_string(cap, lang ='eng') 
        print(tesstr.rsplit("\n",1)[0])
        fastKeyboard(tesstr.rsplit("\n",1)[0])
        time.sleep(0.5)
        checkNextLine()


def endTest():
    userContinue = input("repeat lesson without errors? y/n")
    if userContinue == "y":
        realText = input("paste the text here:")
        time.sleep(10)
        keyboard.write(realText)
        action.has_run = False
        checkNextLine()
    else:
        time.sleep(10)
        action.has_run = False
        checkNextLine()

  

def checkNextLine(): 
    pytesseract.pytesseract.tesseract_cmd =r'C:\\Users\\Public\\Tesseract-OCR\\tesseract.exe'
    while(True): 
        #configure screen area of next line
        cap2 = ImageGrab.grab(bbox =(16, 294, 1628, 366)) 
        #here you can configure language
        nextLine = pytesseract.image_to_string(cap2, lang ='eng') 
        print(nextLine)
        print(len(nextLine))

        if len(nextLine) >= 5:
            imgToString2()
        else:
            action = run_once(imgToString)
            action()
            endTest()
            time.sleep(10)

checkNextLine()      
