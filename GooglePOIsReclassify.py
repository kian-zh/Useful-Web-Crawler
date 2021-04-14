import csv
import codecs

commerce_whole = ['casino', 'bowling_alley', 'amusement_park', 'shopping_mall']
commerce_part = [ 'electrician', 'hardware_store', 'liquor_store', 'drugstore', 'hair_care', 'moving_company', 'book_store', 'accounting', 
            'art_gallery', 'cafe', 'clothing_store', 'atm',
            'bicycle_store', 'car_dealer', 'jewelry_store', 'meal_takeaway', 'pet_store', 'bank', 'car_rental', 'dentist', 'furniture_store',
            'electronics_store', 'laundry', 'pharmacy', 'bar', 'car_repair', 'department_store', 'gas_station', 'lawyer', 'movie_rental', 'physiotherapist'
            'beauty_salon', 'car_wash', 'doctor', 'gym', 'movie_theater', 'real_estate_agency', 'restaurant', 'roofing_contractor',
            'shoe_store', 'spa', 'store', 'supermarket', 'travel_agency', 'veterinary_care', 'night_club', 'home_goods_store','locksmith', 'painter',
            'convenience_store', 'meal_delivery', 'bakery', 'florist', 'insurance_agency'
            ]
community_whole = ['airport', 'cemetery', 'museum', 'church', 'hindu_temple', 'local_government_office',
            'aquarium', 'city_hall', 'embassy', 'fire_station', 'hospital', 'park', 'campground', 'parking', 'courthouse', 'funeral_home'
            'mosque', 'library', 'primary_school', 'rv_park', 'school', 'secondary_school', 'stadium', 'synagogue', 'train_station', 'transit_station',
            'university', 'zoo', 'town_square'
            ]
community_part = ['light_rail_station', 'bus_station', 'police', 'post_office', 'subway_station', 'taxi_stand']
lodging = ['lodging']
storage = ['storage']
tourist_attraction = ['tourist_attraction']
				
						

#
#   高权重类型: lodging  tourist_attraction  storage  community_whole  commerce_whole
#   低权重类型: community_part  commerce_part
#

input = open('rawPOIs.csv')
inputLines = csv.reader(input)

#
#   分类储存在不同的 csv 中 [lodging, tourist_attraction, storage, community_whole, commerce_whole, community_part, commerce_part]
#

typesDic = {}
typesList = ['lodging', 'tourist_attraction', 'storage', 'community_whole', 'commerce_whole', 'community_part', 'commerce_part']
for typeItem in typesList:
    filePath = 'classifiedPOIs\\' + typeItem +'.csv'
    typesDic[typeItem] = codecs.open(filePath,'a','utf-8')
    typesDic[typeItem].write('lat,lon\n')

for i,line in enumerate(inputLines):
    if(i>0):
        types = line[2:]
        type_high = ''
        type_low = ''
        for type in types:
            if type in commerce_whole:
                typesDic['commerce_whole'].write(line[0]+','+line[1]+'\n')
            if type in community_whole:
                typesDic['community_whole'].write(line[0]+','+line[1]+'\n')
            if type in storage:
                typesDic['storage'].write(line[0]+','+line[1]+'\n')
            if type in tourist_attraction:
                typesDic['tourist_attraction'].write(line[0]+','+line[1]+'\n')
            if type in lodging:
                typesDic['lodging'].write(line[0]+','+line[1]+'\n')
        for type in types:
            if type in commerce_part:
                typesDic['commerce_part'].write(line[0]+','+line[1]+'\n')
            if type in community_part:
                typesDic['community_part'].write(line[0]+','+line[1]+'\n')
input.close()
for typeItem in typesList:
    typesDic[typeItem].close()



