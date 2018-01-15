import MySQLdb
import json

db = MySQLdb.connect(host="localhost",
                     user="root",
                     password="0621",
                     #password="Asdu_yu_db.",
                     # db="TRAVEL_TIME_PROCESS")
                     db="Travel_Time_Process")
cursor = db.cursor()

#倒入过滤好的卡口，这些卡口路段全联通
f = open("/Users/migowei/Documents/实验数据/filter_roadID.txt","r")
#f = open("./ancillary_data/filter_roadID.txt", "r")
line = f.readline()
line = f.readline()
while(line):
    line = line.split(",")
    spotID = line[0]
    longitude = line[1]
    latitude = line[2]
    area = line[3]
    times = line[4]
    print(spotID,longitude,latitude,area,times)
    cursor.execute("insert into Filtered_SpotID (spotID, longitude, latitude, area, times) value(%s, %s, %s, %s, %s)", [spotID,longitude,latitude,area,times])
    line = f.readline()
f.close()
cursor.close()
db.autocommit("on")
db.close()


# 倒入道路信息数据
# with open("/Users/migowei/Documents/实验数据/road_info/road_info.json",'r') as load_f:
# with open("./ancillary_data/road_info.json", 'r') as load_f:
#     load_dict = json.load(load_f)
#
# for line in load_dict:
#     print(line)
#     origin = line['from']
#     lngf = line['lngf']
#     latf = line['latf']
#     dest = line['to']
#     lngt = line['lngt']
#     latt = line['latt']
#     dist = line['distance']
#     cursor.execute("insert into road_info (origination, lngf, latf, destination, lngt, latt, dist) value(%s, %s, %s, %s, %s, %s, %s)",[origin, lngf, latf, dest, lngt, latt, dist])
# db.autocommit("on")
# cursor.close()
# db.close()


# f = open("/Users/migowei/Documents/实验数据/road_info/road_info_f_new.json",'w')
# cursor.execute("select * from road_info_f")
# lines = cursor.fetchall()
# jsonData = []
# for line in lines:
#     result = {}
#
#     result['origination'] = line[0]
#     result['lngf'] = line[1]
#     result['latf'] = line[2]
#     result['destination'] = line[3]
#     result['lngt'] = line[4]
#     result['latt'] = line[5]
#     result['dist'] = line[6]
#     print(len(line[3]))
#     if(len(line[3])== 12):
#         jsonData.append(result)
#
# jsonData = json.dumps(jsonData)
# f.write(jsonData)
# f.close()
# cursor.close()
