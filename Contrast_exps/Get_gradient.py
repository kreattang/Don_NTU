#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 11:24
# @Author  : blvin.Don
# @File    : Get_gradient.py


from sklearn import linear_model
import numpy as np
import pandas as pd
from math import atan,degrees,fabs

# 计算斜率
def Get_gradient(positionx,positiony):
    reg = linear_model.LinearRegression()
    # 假设数据是data
    x = np.array([positionx[0],positiony[0]]).reshape(-1,1)
    y = pd.Series([positionx[1],positiony[1]])
    reg.fit(x,y)
    angle = degrees(atan(reg.coef_))
    if angle < 0:
        angle = 180+angle
    else:
        angle = fabs(angle)
    return round(angle,2)

# 斜率为
# print(Get_gradient([0,0],[-1,0]))