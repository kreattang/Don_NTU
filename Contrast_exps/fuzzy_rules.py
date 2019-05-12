#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 2/4/19 8:41 PM
# @Author  : tang
# @File    : fuzzy_rules.py

def fuzzy_control(a):
    if a[0] == 'N' and a[1] == 'M' and a[2] == 'N': return 'M','TLL'
    if a[0] == 'N' and a[1] == 'F' and a[2] == 'N': return 'F','GO'
    if a[0] == 'N' and a[1] == 'N' and a[2] == 'M': return 'S','TR'
    if a[0] == 'N' and a[1] == 'M' and a[2] == 'M': return 'M','TRL'
    if a[0] == 'N' and a[1] == 'F' and a[2] == 'M': return 'F','TRL'
    if a[0] == 'M' and a[1] == 'N' and a[2] == 'N': return 'S','TL'
    if a[0] == 'M' and a[1] == 'M' and a[2] == 'N': return 'M','TLL'
    if a[0] == 'M' and a[1] == 'F' and a[2] == 'N': return 'F','TLL'
    if a[0] == 'M' and a[1] == 'N' and a[2] == 'M': return 'S','TL'
    if a[0] == 'M' and a[1] == 'M' and a[2] == 'M': return 'M','TL'
    if a[0] == 'M' and a[1] == 'F' and a[2] == 'M': return 'F','GO'
    else:
        return None







