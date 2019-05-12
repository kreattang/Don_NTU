#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 17:00
# @Author  : blvin.Don
# @File    : Fuzzy_Rule.py


import operator
def Is_mathch(conflicts,pattern1):
    if (operator.eq(conflicts[0],pattern1[0]) and operator.eq(conflicts[1],pattern1[1])) or (operator.eq(conflicts[0],pattern1[1]) and operator.eq(conflicts[1],pattern1[0])):
        return True
    else:
        return False

def Is_mathch_three(conflicts,pattern1):
    ret = [i for i in conflicts if i not in pattern1]
    if ret:
        return False
    else:
        return True

def Get_HeadingAngle_Velocity(conflicts):
    Conflicts_list = conflicts
    Action = []

    # # 没有冲突
    if len(Conflicts_list) == 0:
        return Action
    # # 只有一个方向有冲突
    elif len(Conflicts_list) == 1:
        if Conflicts_list[0][0] == 'L' and Conflicts_list[0][1] == 'A':
            Action.append('Z')
            Action.append('SU')
        if Conflicts_list[0][0] == 'L' and Conflicts_list[0][1] == 'D':
            Action.append('Z')
            Action.append('SD')
        if Conflicts_list[0][0] == 'F' and Conflicts_list[0][1] == 'A':
            Action.append('PS')
            Action.append('NC')
        if Conflicts_list[0][0] == 'F' and Conflicts_list[0][1] == 'A':
            Action.append('PS')
            Action.append('NC')
        if Conflicts_list[0][0] == 'F' and Conflicts_list[0][1] == 'D':
            Action.append('PB')
            Action.append('SU')
        if Conflicts_list[0][0] == 'R' and Conflicts_list[0][1] == 'A':
            Action.append('Z')
            Action.append('SD')
        if Conflicts_list[0][0] == 'R' and Conflicts_list[0][1] == 'D':
            Action.append('PS')
            Action.append('SD')

    elif len(Conflicts_list) == 2:
        if Is_mathch(Conflicts_list,[['L','A'],['F','A']]):
            Action.append('Z')
            Action.append('NC')
        if Is_mathch(Conflicts_list,[['L','A'],['F','D']]):
            Action.append('Z')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['L','D'],['F','A']]):
            Action.append('Z')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['L','D'],['F','D']]):
            Action.append('PS')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['R','A'],['F','A']]):
            Action.append('PS')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['R','A'],['F','D']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['R','D'],['F','A']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['R','D'],['F','D']]):
            Action.append('PB')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['L','A'],['R','A']]):
            Action.append('PS')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['L','A'],['R','D']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['L','D'],['R','A']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch(Conflicts_list,[['L','D'],['R','D']]):
            Action.append('PB')
            Action.append('SD')
    elif len(Conflicts_list) == 3:
        if Is_mathch_three(Conflicts_list,[['L','A'],['R','A'],['F','A']]):
            Action.append('Z')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','D'],['R','A'],['F','A']]):
            Action.append('PS')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','A'],['R','D'],['F','A']]):
            Action.append('PS')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','A'],['R','A'],['F','D']]):
            Action.append('PS')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','D'],['R','D'],['F','A']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','D'],['R','A'],['F','D']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','A'],['R','D'],['F','D']]):
            Action.append('PM')
            Action.append('SD')
        if Is_mathch_three(Conflicts_list,[['L','D'],['R','D'],['F','D']]):
            Action.append('PB')
            Action.append('SD')
    return Action