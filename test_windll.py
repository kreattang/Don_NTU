#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 15:11
# @Author  : blvin.Don
# @File    : test_windll.py



import pymouse,pykeyboard,os,sys
import time
from pymouse import *
from pykeyboard import PyKeyboard
m = PyMouse()
k = PyKeyboard()



count = 0
while count < 8:
    time.sleep(30)
    x, y = m.position()
    for i in range(10):
        m.click(x, y)
        y = y + 27
        time.sleep(3)
    count = count +1



