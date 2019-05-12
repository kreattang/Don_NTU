#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 17:05
# @Author  : blvin.Don
# @File    : main.py

from  read_all_xml import Get_all_name
from  xml_to_json import xml2json
from detection import detector

filePath = '/home/wenbing/Desktop/Don_NTU/CNVD_dataset'
names = Get_all_name(filePath)
# print(names)
for name in names[1:]:
    xml2json(name)