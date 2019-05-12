#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 20:01
# @Author  : blvin.Don
# @File    : Get_distance.py


import math

def get_distance(poistion1,position2):
    return round(math.sqrt((poistion1[0] - position2[0]) ** 2 + (poistion1[1] - position2[1]) ** 2),5)

# print(get_distance([233,233],[223,278]))