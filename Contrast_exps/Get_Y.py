#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 14:10
# @Author  : blvin.Don
# @File    : Get_Y.py
from math import tan,pi
def get_y(x,theta,given_point):
    k = tan(theta*pi/180)
    y = round(k*x-k*given_point[0]+given_point[1],2)
    return x,y
