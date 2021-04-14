# 从谷歌API获取POI
import urllib.request 
from urllib.parse import quote 
import string
import json
import codecs
#import numpy


baseURL = "https://www.fazwaz.com/property-for-sale/thailand/bangkok?type=property&zoomLevel=9&center={0}&bound={1}&action=markers"

center = "13.717330737954512,100.8430965227866"
bound = "14.053286711862519,101.8867976946616:13.380893237374746,99.79939535091158"

URL = baseURL.format(center,bound)
URL = "https://www.fazwaz.com/property-for-sale/thailand/bangkok?type=property&zoomLevel=9&center=13.717330737954512,100.8430965227866&bound=14.053286711862519,101.8867976946616:13.380893237374746,99.79939535091158&action=markers"
outfile = 'output.csv'

csvFile=codecs.open(outfile,'a','utf-8')
csvFile.write('lat,lon\n')

headers = {
    'Host': 'www.fazwaz.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Origin': 'http://sgis.site',
    'Connection': 'keep-alive',
    'Referer': 'http://sgis.site/'
}

req = urllib.request.Request(url=URL, headers=headers)
res = urllib.request.urlopen(req)
response = res.read().decode('utf-8')
responseJSON = json.loads(response)
markers = responseJSON['markers']
for item in markers:
    coordinates = item['point']['coordinates']
    csvFile.write(str(coordinates[1]) + ',' + str(coordinates[0]) + '\n')
csvFile.close()
print('结束')
