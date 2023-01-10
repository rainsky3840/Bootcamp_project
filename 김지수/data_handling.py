import json
import glob
import cv2

dir_1 = glob.glob('01.데이터/1.Training/라벨링데이터/단일경구약제 5000종/*')
dir_j = []
for temp_dir in dir_1:
    dir_j += glob.glob(temp_dir + '/*.*')
print(len(dir_j))
# dir_json = '01.데이터/1.Training/라벨링데이터/단일경구약제 5000종/K-038884_json/K-038884_0_0_0_0_75_000_200.json'

temp_img_dir = glob.glob('01.데이터/1.Training/원천데이터/단일경구약제 5000종/*')
print(temp_img_dir)
# for img_dir in temp_img_dir:  # temp_dir이 경구약제 5000종 바로 아래 경로임.
#
#     with open(dir_json, 'r', encoding='UTF-8') as j:
#
#         json_data = json.load(j)
#         file_name = json_data['images'][0]['file_name']
#         # img = cv2.imread(img_dir+file_name, cv2.IMREAD_COLOR)
#         # print(img)
#         file_dir = []
#
#         print(img_dir + file_name, i)
#         print(json_data['annotations'][0]['bbox'])  # x, y, w, h