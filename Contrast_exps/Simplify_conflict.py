#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 15:07
# @Author  : blvin.Don
# @File    : Simplify_conflict.py


def deal_conflicts(confllicts):
    temp = []
    if len(confllicts) == 0:
        pass
    elif len(confllicts) == 1:
        return confllicts[0][:-1]
    else:
        max_ROC = confllicts[0][-1]
        for i in confllicts:
            if i[-1] >= max_ROC:
                temp = i[:-1]
                max_ROC = i[-1]
        return temp



def simplify_conflict_by_ROC(confllicts):
    confllict_L = []
    confllict_F = []
    confllict_R = []
    final_conflict = []
    for c in confllicts:
        if c[0] == 'L':
            confllict_L.append(c)
        if c[0] == 'F':
            confllict_F.append(c)
        if c[0] == 'R':
            confllict_R.append(c)
    for co in confllict_L,confllict_F,confllict_R:
        if deal_conflicts(co):
            final_conflict.append(deal_conflicts(co))
    return final_conflict