#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:19
# @Author  : blvin.Don
# @File    : Relative_Loaction_Turtle.py
from math import fabs
from Contrast_exps.Get_Angle_TwoVec import Get_Angle_Between_Two_Vector

def Get_Relative_Location(owner,intruder,heading):
    angle = Get_Angle_Between_Two_Vector([350,owner[1]],[intruder[0],intruder[1]],[owner[0],owner[1]])
    if intruder[1] < owner[1]:
        angle = 360 - angle
    elif  intruder[1] > owner[1] :
        angle = angle
    elif intruder[1] == owner[1]:
        if intruder[0] > owner[0]:
            angle = 0
        else:
            angle = 180

    # print(angle)
    if fabs(angle - heading) < 30:
        return 'F'
    else:
        if heading-90 <angle < heading-20:
            return 'R'
        elif heading+100>angle > heading+20:
            return 'L'


# print(Get_Relative_Location([0,0],[0,-110],225))