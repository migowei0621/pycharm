import os

#获取数据文件列表
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    all_file =[]
    for allfile in pathDir:
        eachf = os.path.join(filepath, allfile)
        all_file.append(eachf)
    return all_file[:1]

def readData(filepath):
    file = "/Users/migowei/Documents/实验数据/vehicleInfoMap.txt"
    fw = open(file, 'w')
    all_file = eachFile(filepath)
    vehicle_info_map = {}
    for e in all_file:
        fr = open(e, 'r')
        for line in fr.readlines():
            line = line.split(',')
            key = line[0]
            value = [line[2],line[3],line[5]]
            if key not in vehicle_info_map.keys():
                vehicle_info_map[key] = [value]
            else:
                vehicle_info_map[key].append(value)
            print(str(key) + str(vehicle_info_map[key]))
            fw.writelines(str(key) + str(vehicle_info_map[key]) + "\n")
    fr.close()
    fw.close()
    return vehicle_info_map


if __name__ == '__main__':

    filepath = "/Users/migowei/Documents/实验数据/C"
    vehicleMap=readData(filepath)
