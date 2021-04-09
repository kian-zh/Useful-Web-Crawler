# 从谷歌API获取POI
import urllib.request 
from urllib.parse import quote 
import string
import json
import codecs
import numpy

# 参数
lonRange = [100.76, 100.85]  # the range of longitude 经度的范围 //100.15-100.85
latRange = [13.50, 14]  # the range of latitude 纬度的范围  //14
lonDivision = 0.005 # 分块查询 经度方向合计大约60km 每格约0.4km
latDivision = 0.005 # 分块查询 纬度方向合计大约40km 每格约0.4km
radius = 500 # 查询参数 半径 500m
TIMEOUT = 30
outfile = "output.csv"

#   Google Key
googleKey = "谷歌Key"

#restaurant_j = json_format(res_test)
print('开始爬取')
print('共有'+str(((lonRange[1]-lonRange[0])/lonDivision+1)*((latRange[1]-latRange[0])/latDivision+1))+'次请求')
count = 0
countLine = 0

place_id_list = []
csvFile=codecs.open(outfile,'a','utf-8')
csvFile.write('lat,lon,types\n')

for lon in numpy.arange(lonRange[0], lonRange[1], lonDivision):
    print('已进行'+str(count)+'次请求，得到'+str(countLine)+'条有效信息')
    for lat in numpy.arange(latRange[0], latRange[1], latDivision):
        print('已进行'+str(count)+'次请求，得到'+str(countLine)+'条有效信息')
        #   发请求
        latlon = str(lat)+','+str(lon)
        basic_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={0}&location={1}&radius={2}'  
        url = basic_url.format(googleKey,latlon,radius)
        url = quote(url, safe = string.printable)
        req = urllib.request.urlopen(url,timeout=TIMEOUT)
        response = req.read().decode('utf-8')
        responseJSON = json.loads(response)
        for item in responseJSON['results']:
            #对每个POI
            place_id = item['place_id']
            types = item['types']
            #如果id不在已有的list里
            if not place_id in place_id_list:
                #如果类型中有point_of_interest
                if "point_of_interest" in types:
                    place_id_list.append(place_id)
                    line = str(item['geometry']['location']['lat']) + ',' + str(item['geometry']['location']['lng'])
                    for type in types:
                        line = line + ',' + str(type)
                    csvFile.write(line + '\n')
                    countLine = countLine + 1
        count = count + 1
csvFile.close()
print('结束')
