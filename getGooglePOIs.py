# �ӹȸ�API��ȡPOI
import urllib.request 
from urllib.parse import quote 
import string
import json
import codecs
import numpy

# ����
lonRange = [100.76, 100.85]  # the range of longitude ���ȵķ�Χ //100.15-100.85
latRange = [13.50, 14]  # the range of latitude γ�ȵķ�Χ  //14
lonDivision = 0.005 # �ֿ��ѯ ���ȷ���ϼƴ�Լ60km ÿ��Լ0.4km
latDivision = 0.005 # �ֿ��ѯ γ�ȷ���ϼƴ�Լ40km ÿ��Լ0.4km
radius = 500 # ��ѯ���� �뾶 500m
TIMEOUT = 30
outfile = "output.csv"

#   Google Key
googleKey = "�ȸ�Key"

#restaurant_j = json_format(res_test)
print('��ʼ��ȡ')
print('����'+str(((lonRange[1]-lonRange[0])/lonDivision+1)*((latRange[1]-latRange[0])/latDivision+1))+'������')
count = 0
countLine = 0

place_id_list = []
csvFile=codecs.open(outfile,'a','utf-8')
csvFile.write('lat,lon,types\n')

for lon in numpy.arange(lonRange[0], lonRange[1], lonDivision):
    print('�ѽ���'+str(count)+'�����󣬵õ�'+str(countLine)+'����Ч��Ϣ')
    for lat in numpy.arange(latRange[0], latRange[1], latDivision):
        print('�ѽ���'+str(count)+'�����󣬵õ�'+str(countLine)+'����Ч��Ϣ')
        #   ������
        latlon = str(lat)+','+str(lon)
        basic_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={0}&location={1}&radius={2}'  
        url = basic_url.format(googleKey,latlon,radius)
        url = quote(url, safe = string.printable)
        req = urllib.request.urlopen(url,timeout=TIMEOUT)
        response = req.read().decode('utf-8')
        responseJSON = json.loads(response)
        for item in responseJSON['results']:
            #��ÿ��POI
            place_id = item['place_id']
            types = item['types']
            #���id�������е�list��
            if not place_id in place_id_list:
                #�����������point_of_interest
                if "point_of_interest" in types:
                    place_id_list.append(place_id)
                    line = str(item['geometry']['location']['lat']) + ',' + str(item['geometry']['location']['lng'])
                    for type in types:
                        line = line + ',' + str(type)
                    csvFile.write(line + '\n')
                    countLine = countLine + 1
        count = count + 1
csvFile.close()
print('����')
