#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 16:10
# @Author  : blvin.Don
# @File    : Get_Angle_TwoVec.py
import numpy as np

def Get_Angle_Between_Two_Vector(Vec1,Vec2,Std):
    # print(Vec1,Vec2,Std)
    x = np.array([Vec1[0], Vec1[1]])
    y = np.array([Vec2[0], Vec2[1]])
    std = np.array([Std[0], Std[1]])
    x = x - std
    y = y - std
    # 两个向量
    Lx = np.sqrt(x.dot(x))
    Ly = np.sqrt(y.dot(y))
    # 相当于勾股定理，求得斜线的长度
    cos_angle = x.dot(y) / (Lx * Ly)
    # 求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。。
    # print(cos_angle)
    angle = np.arccos(cos_angle)
    angle2 = angle * 360 / 2 / np.pi
    # 变为角度
    return round(angle2,2)

# print(Get_Angle_Between_Two_Vector([243, 257],[259, 257],[257, 257]))