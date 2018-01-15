import os
from datetime import datetime, timedelta

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    all_file = []
    for allfile in pathDir:
        eachf = os.path.join(filepath,allfile)
        all_file.append(eachf)

    return all_file


def process(all_file):
    roadtimeMap = {}
    for file in all_file:
        fr = open(file,'r')
        for line in fr:
            key = line.split("#")[1]
            value = (line.split("#")[0],line.split("#")[2].strip('[').split(',')[0],line.split("#")[2].strip().strip(']').split(',')[1])
            if key not in roadtimeMap.keys():
                roadtimeMap[key] = [value]
            else:
                roadtimeMap[key].append(value)
        fr.close()
    return roadtimeMap


## Filling data with normal pass time when there have no value at some time slots.
def filling(roadtimeMap):
    NORMAL_PASS_TIME = 30
    roadtimeFillingMap = {}
    timeS = datetime.strptime("2015-12-01 00:00:00","%Y-%m-%d %H:%M:%S")
    timeE = datetime.strptime("2016-02-29 23:45:00","%Y-%m-%d %H:%M:%S")
    # timeE = datetime.strptime("2016-01-31 23:45:00","%Y-%m-%d %H:%M:%S")
    # timeE = datetime.strptime("2015-12-31 23:45:00","%Y-%m-%d %H:%M:%S")

    for key in roadtimeMap:
        time = timeS
        while(time<=timeE):
            if(len(roadtimeMap[key])):
                #print(datetime.strptime(roadtimeMap[key][0][0].split('~')[0].strip('['), "%Y-%m-%d %H:%M:%S"))
                if(time == datetime.strptime(roadtimeMap[key][0][0].split('~')[0].strip('['),"%Y-%m-%d %H:%M:%S")):
                    if key not in roadtimeFillingMap.keys():
                        roadtimeFillingMap[key] = [roadtimeMap[key][0]]
                    else:
                        roadtimeFillingMap[key].append(roadtimeMap[key][0])
                    del(roadtimeMap[key][0])

                else:
                    k = "~".join((str(datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)),
                              str(datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
                                  + timedelta(minutes=15))))
                    k = '['+ k +')'
                    if key not in roadtimeFillingMap:
                        roadtimeFillingMap[key] = [[k,NORMAL_PASS_TIME,'@']]
                    else:
                        roadtimeFillingMap[key].append([k,NORMAL_PASS_TIME,'@'])
            else:
                k = "~".join((str(datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)),
                              str(datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
                                  + timedelta(minutes=15))))
                k = '[' + k + ')'
                if key not in roadtimeFillingMap:
                    roadtimeFillingMap[key] = [[k, NORMAL_PASS_TIME, '@']]
                else:
                    roadtimeFillingMap[key].append([k, NORMAL_PASS_TIME, '@'])

            time = time + timedelta(minutes=15)

    return roadtimeFillingMap



if __name__ == '__main__':
    filepath = "/Users/migowei/Documents/实验数据/avg_travel_time_sorted/thresHold_60"
    # filepath = "/home/migo/avg_travel_time_sorted/thresHold_60"

    all_file = eachFile(filepath)
    roadtimeMap = process(all_file)
    roadtimeFillingMap = filling(roadtimeMap)

    # for i in roadtimeFillingMap:
    #     # print("%s : %s " % (i, roadtimeFillingMap[i]))
    #     # print("%s:" % i,end='')
    #     # for item in roadtimeFillingMap[i]:
    #     #     print(item[1],end=' ')
    #     # print()
    #     print("%s:" % i, end='')
    #     line = ''
    #     for item in roadtimeFillingMap[i]:
    #         line = line + str(item[1]) + ' '
    #     print(line)

    for key in roadtimeFillingMap:
        # filew = "/home/migo/TraveltimeList/"+ key +".txt"
        # filew = "/Users/migowei/Documents/实验数据/30_padding/TestSet/1months/"+ key + ".txt"
        filew = "/Users/migowei/Documents/实验数据/TraveltimeList/" + key + ".txt"
        line = ''
        for item in roadtimeFillingMap[key]:
            line = line + str(item[1]) + ' '

        fw = open(filew,'w')
        fw.write(line)
        fw.close()


