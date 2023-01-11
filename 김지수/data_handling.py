import json
import glob
import cv2
import os

dir_1 = glob.glob('Data/1.Training/labeling_data/drug/*')
json_names = []
for temp_dir in dir_1:
    json_names += glob.glob(temp_dir + '/*.*')
# print(json_names[:3])

temp_img_dir = glob.glob('Data/1.Training/raw_data/drug/*')
# print(len(temp_img_dir))
img_names = []
for temp in temp_img_dir:
    img_names += glob.glob(temp + '/*.*')

# print(img_names[:10])
i = 0
# os.mkdir('Data/1.Training/images/' + 'hi')
for idx, img_data in enumerate(json_names):
    img_data = img_data.replace('\\', '/', 10)
    # print(img_data)
    with open(img_data, 'r', encoding='UTF=8') as j:
        js = json.load(j)
        file_name = js['images'][0]['file_name']
        file_dir = 'Data/1.Training/images/' + file_name[:8]
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)

        file_dir = file_dir + '/' + file_name

        if not os.path.isfile(file_dir):
            # print(file_dir)
            x, y, w, h = js['annotations'][0]['bbox']

            cx = x + w // 2
            cy = y + h // 2
            w_h, h_h = max(w, h), max(w, h)  # 깨끗한 data 를 얻기 위해 크롭영역을 정방형으로 해준다. 기준은 둘 중 큰 값
            x = cx - (w_h // 2)
            y = cy - (h_h // 2)

            # print(x, y, w, h)
            img_names[idx] = img_names[idx].replace('\\', '/', 10)
            # print(img_names[idx])
            img = cv2.imread(img_names[idx], cv2.IMREAD_COLOR)
            cropped_img = img[y:y + h_h, x:x + w_h]
            cropped_img = cv2.resize(cropped_img, (64, 64))
            if idx % 100 == 0:
                print('진행상황: {} / {}'.format(idx, len(img_names)))
            cv2.imwrite(file_dir, cropped_img)
        else:
            print('이미 처리한 데이터 입니다.')
            continue
