#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 19:52
# @Author  : blvin.Don
# @File    : Crossover_point.py
from Contrast_exps.cross_point import cross_point
def Get_crossover_point(Line_set):
    temp = []
    for i in range(len(Line_set)):
        for j in range(i + 1, len(Line_set)):
            # print(Line_set[i],Line_set[j])
            temp1 = []
            for li in Line_set[i]:
                temp1 = temp1+li
            temp2 = []
            for lj in Line_set[j]:
                temp2 = temp2 + lj
            # print(temp1,temp2)
            temp.append(cross_point(temp1,temp2))
    return temp

# Line_set = [[[33.71472042450364, -80.39851752096108], [-350, 182.78]], [[33.71472042450364, -80.39851752096108], [-350, 20185.49]], [[33.79670523066844, -77.9981143875334], [-350, -904.42]], [[33.79670523066844, -77.9981143875334], [-350, -38699.45]]]
# #
# # print(len(Line_set))
# # for L in Line_set:
# #     print(L)
#
# print(Get_crossover_point(Line_set))

