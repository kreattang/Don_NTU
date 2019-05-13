#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 19-5-12 下午3:50
# @Author  : tang
# @File    : URL_Legal.py


import sys
import re
def is_legal(url):
#Make sure we have a single URL argument.
    # if len(sys.argv) != 2:
    #     print (sys.stderr, "URL Required")
    #     sys.exit(-1)
    # #Easie access.
    # url = sys.argv[1]
    #Ensure we were passed a somewhat valid URL.
    #This is a superficial test.
    if re.match(r'^https?:/{2}\w.+$', url):
        return True
    else:
        return False


