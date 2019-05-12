#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 2/4/19 9:04 PM
# @Author  : tang
# @File    : defuzzificztion.py

def defuzzificztion(output):
    o = output
    # print("THEN:",output)
    speed = 0
    yaw = 0
    if o[0] == 'M':
        speed = 4
    if o[0] == 'S':
        speed = 2
    if o[0] == 'F':
        speed =6
    if o[1] == 'GO':
        yaw = 0
    if o[1] == 'TRL':
        yaw = 30
    if o[1] == 'TR':
        yaw = 60
    if o[1] == 'TLL':
        yaw = -30
    if o[1] == 'TL':
        yaw = -60
    return speed,yaw