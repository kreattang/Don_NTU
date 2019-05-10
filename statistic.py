from read_all_xml import Get_all_name
from xml_to_json import xml2json

file_name = Get_all_name

for name in file_name[:1]:
    total, nvd = xml2json(name)
    print(total, nvd)