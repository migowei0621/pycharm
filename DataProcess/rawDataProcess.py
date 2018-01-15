import os
import MySQLdb
from datetime import datetime, timedelta


# 获取数据文件列表
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    all_file = []
    for allfile in pathDir:
        eachf = os.path.join(filepath, allfile)
        all_file.append(eachf)
    return all_file[0:2]
    # return all_file[2:3]


def readData(filepath):
    vehicle_info_map = {}
    fr = open(filepath,'r')
    count = 0
    for line in fr.readlines():
        line = line.split(',')
        key = line[0]
        value = [line[2],line[3],line[5]]
        if key not in vehicle_info_map.keys():
            vehicle_info_map[key] = [value]
        else:
            vehicle_info_map[key].append(value)
            count += 1
            # print(count)
    fr.close()
    return vehicle_info_map


def matchRoad(map):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         password="0621",
                         # password="Asdu_yu_db.",
                         db="TRAVEL_TIME_PROCESS")
                         # db="Travel_Time_Process")
    cursor = db.cursor()
    time_road_Map = {}
    avg = 0
    num = 0
    THRESHOLD = 60*60
    for key in map:
        if len(map[key]) != 1:
            index = 0
            for one in map[key]:
                if index < len(map[key]) - 1:
                    re = cursor.execute("select * from road_info_f where origination = %s and destination = %s",
                                        [map[key][index][0], map[key][index + 1][0]])
                    if re != 0:
                        time1 = datetime.strptime(str(map[key][index][2]).strip(), "%Y-%m-%d %H:%M:%S %f")
                        time2 = datetime.strptime(str(map[key][index + 1][2]).strip(), "%Y-%m-%d %H:%M:%S %f")
                        if abs(time1.hour-time2.hour) <=2:
                            if  time1.minute >= 00 and time1.minute < 15 and (time2-time1).total_seconds() <= THRESHOLD:
                                k = "~".join((str(datetime(time1.year, time1.month, time1.day, time1.hour, 00, 00)),
                                              str(datetime(time1.year, time1.month, time1.day, time1.hour, 15, 00))))
                                k = "[" + k + ")"
                                key_road = str(map[key][index][0]) + "~" + str(map[key][index + 1][0])
                                if k not in time_road_Map:
                                    avg = (time2 - time1).total_seconds()
                                    num = 1
                                    # time_road_Map[k] = { key_road : [time2-time1]}
                                    time_road_Map[k] = {key_road: [avg, num]}
                                else:
                                    if key_road not in time_road_Map[k]:
                                        avg = (time2 - time1).total_seconds()
                                        num = 1
                                        # time_road_Map[k][key_road] = [time2-time1]
                                        time_road_Map[k][key_road] = [avg, num]
                                    else:
                                        num = time_road_Map[k][key_road][1] + 1
                                        avg = (time_road_Map[k][key_road][0] * time_road_Map[k][key_road][1] + (
                                        time2 - time1).total_seconds()) / num
                                        # time_road_Map[k][key_road].append(time2-time1)
                                        time_road_Map[k][key_road] = [avg, num]
                                # print(time_road_Map[k][key_road])

                            elif time1.minute >= 15 and time1.minute < 30 and (time2-time1).total_seconds() <= THRESHOLD:

                                k = "~".join((str(datetime(time1.year, time1.month, time1.day, time1.hour, 15, 00)),
                                              str(datetime(time1.year, time1.month, time1.day, time1.hour, 30, 00))))
                                k = "[" + k + ")"
                                key_road = str(map[key][index][0]) + "~" + str(map[key][index + 1][0])
                                if k not in time_road_Map:
                                    avg = (time2 - time1).total_seconds()
                                    num = 1
                                    # time_road_Map[k] = {key_road: [time2 - time1]}
                                    time_road_Map[k] = {key_road: [avg, num]}
                                else:
                                    if key_road not in time_road_Map[k]:
                                        avg = (time2 - time1).total_seconds()
                                        num = 1
                                        # time_road_Map[k][key_road] = [time2 - time1]
                                        time_road_Map[k][key_road] = [avg, num]
                                    else:
                                        num = time_road_Map[k][key_road][1] + 1
                                        avg = (time_road_Map[k][key_road][0] * time_road_Map[k][key_road][1] + (
                                        time2 - time1).total_seconds()) / num
                                        # time_road_Map[k][key_road].append(time2 - time1)
                                        time_road_Map[k][key_road] = [avg, num]

                            elif time1.minute >= 30 and time1.minute < 45 and (time2-time1).total_seconds() <= THRESHOLD:
                                k = "~".join((str(datetime(time1.year, time1.month, time1.day, time1.hour, 30, 00)),
                                              str(datetime(time1.year, time1.month, time1.day, time1.hour, 45, 00))))
                                k = "[" + k + ")"
                                key_road = str(map[key][index][0]) + "~" + str(map[key][index + 1][0])
                                if k not in time_road_Map:
                                    avg = (time2 - time1).total_seconds()
                                    num = 1
                                    # time_road_Map[k] = {key_road: [time2 - time1]}
                                    time_road_Map[k] = {key_road: [avg, num]}
                                else:
                                    if key_road not in time_road_Map[k]:
                                        avg = (time2 - time1).total_seconds()
                                        num = 1
                                        # time_road_Map[k][key_road] = [time2 - time1]
                                        time_road_Map[k][key_road] = [avg, num]
                                    else:
                                        num = time_road_Map[k][key_road][1] + 1
                                        avg = (time_road_Map[k][key_road][0] * time_road_Map[k][key_road][1] + (
                                        time2 - time1).total_seconds()) / num
                                        # time_road_Map[k][key_road].append(time2 - time1)
                                        time_road_Map[k][key_road] = [avg, num]

                            elif time1.minute >= 45  and (time2-time1).total_seconds() <= THRESHOLD:
                                # print((time2-time1).total_seconds())
                                k = "~".join((str(datetime(time1.year, time1.month, time1.day, time1.hour, 45, 00)),
                                              str(datetime(time1.year, time1.month, time1.day, time1.hour, 00,
                                                           00) + timedelta(hours=1))))
                                k = "[" + k + ")"
                                key_road = str(map[key][index][0]) + "~" + str(map[key][index + 1][0])
                                if k not in time_road_Map:
                                    avg = (time2 - time1).total_seconds()
                                    num = 1
                                    # time_road_Map[k] = {key_road: [time2 - time1]}
                                    time_road_Map[k] = {key_road: [avg, num]}
                                else:
                                    if key_road not in time_road_Map[k]:
                                        avg = (time2 - time1).total_seconds()
                                        num = 1
                                        time_road_Map[k][key_road] = [avg, num]
                                        # time_road_Map[k][key_road] = [time2 - time1]
                                    else:
                                        num = time_road_Map[k][key_road][1] + 1
                                        avg = (time_road_Map[k][key_road][0] * time_road_Map[k][key_road][1] + (
                                        time2 - time1).total_seconds()) / num
                                        time_road_Map[k][key_road] = [avg, num]
                                        # time_road_Map[k][key_road].append(time2 - time1)
                                # print(time_road_Map[k][key_road])

                    index += 1
    return time_road_Map


if __name__ == '__main__':

    filepath = "/Users/migowei/Documents/实验数据/C"
    # filepath = "/home/chyang/dh/chenandy/data"

    all_file = eachFile(filepath)

    for e in all_file:
        print(e)
        vehicleMap = readData(e)
        time_road_map = matchRoad(vehicleMap)

        name = e.split('/')[6].split('.')[0]
        filew ="/Users/migowei/Documents/实验数据/"+ name + "-avg_travel_time.txt"
        # filew ="/home/migo/avg_travel_time/"+ name + "-avg_travel_time.txt"

        fw = open(filew, 'w')


        dict = sorted(time_road_map.items(), key=lambda d: d[0], reverse=False)
        for k1, value1 in dict:
            dict2 = sorted(time_road_map[k1].items(), key=lambda d:d[0], reverse=False)
            for k2,value2 in dict2:
                fw.write(str(k1) + "#" + str(k2) + "#" + str(time_road_map[k1][k2]) +"\n")
        fw.close()

