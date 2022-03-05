# png 二值图像转点阵txt


import cv2

img = cv2.imread('./R-C.png',0)

ylen = len(img)
xlen = len(img[0])

data = ''
for x in range(120):
    for y in range(90):
        imgX = round((xlen/120)*x)
        imgY = round((ylen/90)*y)
        v = img[imgY][imgX]
        if(v == 188):
            data += '1'
        else:
            data += '0'
    data += ','

with open('map.txt', 'w') as mapTxt:
    mapTxt.write(data)
