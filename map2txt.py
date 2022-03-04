# png 二值图像转点阵txt


import cv2

img = cv2.imread('./R-C.png',0)

ylen = len(img) # 2480
xlen = len(img[0])# 4378

data = ''
for x in range(160):
    for y in range(120):
        imgX = round((4378/160)*x)
        imgY = round((2480/120)*y)
        v = img[imgY][imgX]
        if(v == 188):
            data += '1'
        else:
            data += '0'
    data += ','

with open('map.txt', 'w') as mapTxt:
    mapTxt.write(data)
