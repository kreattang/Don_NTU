
import os

def Get_all_name(filePath):
    file_names = []
    for i in os.listdir(filePath):
        file_names.append(i)
    return file_names

