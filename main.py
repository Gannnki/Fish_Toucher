#!-*-coding:utf-8 -*-
import time
import random
import pyautogui

def random_mouse():
    while 1:
        # change to any time you want
        time.sleep(5)
        pyautogui.moveTo(x=1500,y=random.randint(100,900))
        pyautogui.click()