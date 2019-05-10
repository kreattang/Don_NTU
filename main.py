#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 17:05
# @Author  : blvin.Don
# @File    : main.py

from  read_all_xml import Get_all_name
from  xml_to_json import xml2json
from detection import detector

filePath = 'I:/PycharmProjects/NTU_CNVD/CNVD_dataset'
names = Get_all_name(filePath)
for name in names:
    xml2json(name)