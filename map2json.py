# png 二值图像转点阵


import cv2
import json

img = cv2.imread('./R-C.png',0)

ylen = len(img) # 2480
xlen = len(img[0])# 4378

data = []
for x in range(160):
    for y in range(120):
        imgX = round((4378/160)*x)
        imgY = round((2480/120)*y)
        v = img[imgY][imgX]
        if(v == 188):
            data.append({'x':x,'y':y})
print(data)

json_str = json.dumps(data)

with open('map.json', 'w') as json_file:
    json_file.write(json_str)
