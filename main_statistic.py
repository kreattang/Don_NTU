from  read_all_xml import Get_all_name
from  xml_to_json import xml2json
import pandas as pd

# name_attribute = ['NumberID','UserID','ModuleID','StartDate','EndDate','Frequent']


filePath = 'I:/PycharmProjects/NTU_CNVD/CNVD_dataset'
names = Get_all_name(filePath)
total, ref, nvd, non_nvd = 0, 0, 0, 0
for name in names:
    t, r, n, no = xml2json(name)
    total = total + t
    ref = ref + r
    nvd = nvd + n
    non_nvd = non_nvd + no

print("一共{}条记录，其中包含referenceLink的有{}条,是nvd的有{}条,不是nvd的有{}条.".format(total, ref, nvd, non_nvd))

# 一共42547条记录，其中包含referenceLink的有37737条,是nvd的有7978条,不是nvd的有29758条.
# 还有一条referenceLink字段为None