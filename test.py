#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 19-5-12 下午4:11
# @Author  : tang
# @File    : test.py

import requests

r = requests.get('http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1145')
