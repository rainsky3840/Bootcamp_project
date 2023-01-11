import json
import glob
import cv2
import os
import numpy as np

e = len('/K-039146_json/K-039146_0_0_0_0_60_000_200.json')
s = len('C:/Users/Chaddol/Downloads/166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터/01.데이터/1.Training/라벨링데이터/단일경구약제 5000종/')
print(s, e)

dirs = 'C:/Users/Chaddol/Downloads/166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터/01.데이터/1.Training/라벨링데이터/단일경구약제 5000종'
# dirs = dirs.replace('\\', '/', 10)
dirs_in = glob.glob(dirs + '/*')
print(len(dirs_in))
set_name = []
for s in dirs_in:  #set_name 은 TL_00_단일 이런 형식
    set_name += glob.glob(s + '/*')

print(set_name[0])
files = []
data_set = []
for name in set_name:
    f = name[len(name)-13:len(name)-5] + '_0_0_0_0_60_000_200.json'

    file = name + '/' + f
    file = file.replace('\\', '/', 10)
    data_set_name = file[99 : len(file) - 47]
    # print(file)
    try:
        with open(file, 'r', encoding='UTF-8') as j:
            js = json.load(j)
            # print(js)
            di_class = js['images'][0]['di_class_no']
            if di_class == "[02140]혈압강하제":
                target = js['images'][0]['file_name'][:8]
                files.append(target)
                data_set.append(data_set_name)
                print(file)
    except FileNotFoundError:
        continue

data_set = set(data_set)
print(data_set)
print(files)