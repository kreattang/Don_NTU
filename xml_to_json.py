# -*- coding: UTF-8 -*-
import json
import xmltodict
from detection import detector


def xml2json(file_name):
    # total_member, ref, nvd, non_nvd = 0, 0, 0, 0
    with open('/home/wenbing/Desktop/Don_NTU/CNVD_dataset/'+file_name, 'r', encoding='UTF-8') as f:
        xmlString = f.read()
    jsonString = json.dumps(xmltodict.parse(xmlString),ensure_ascii=False, indent=4)
    output = json.loads(jsonString)
    member = output['vulnerabilitys']['vulnerability']
    for _ in member:
        # total_member = total_member +1
        if 'referenceLink' in _:
            url = _['referenceLink']
            print("链接：", url)
            print(detector(url))