

"""
 count missing spotID for all of the Linyi aria data
"""
def missingSpotData(filePath1,filePath2, out_file_name):
    f1 = open(filePath1,'r')
    f2 = open(filePath2,'r')
    traj_data = f1.readlines()
    info_data = f2.readlines()
    f1.close()
    f2.close()
    # print(traj_data[0])
    fw = open(out_file_name, 'w')
    lst =[]
    for line in traj_data:
        spotID = line.split(',')[2]
        flag = False
        for l in info_data:
            if spotID in l:
                flag = True
        if not flag:
            lst.append(spotID)

    lst = {}.fromkeys(lst).keys()
    fw.writelines(lst)
    fw.close()



def dataExtractor(filePath):
    f = open(filePath,'r')
    f.readline()
    for line in f.readlines():
        # print(int(line.replace('"','').split()[2]))
        if(int(line.replace('"','').split()[2]) == 1):
            print(line.split()[0])




def main():
    data_file_path = "/Users/migowei/Documents/实验数据/C/2015-12-01.txt"
    road_info_file_path = "/Users/migowei/Documents/实验数据/道路txt/road_info.txt"
    out_file_name = "miss_spot.txt"
    missingSpotData(data_file_path, road_info_file_path, out_file_name)

    bay_file_path = "/Users/migowei/Documents/实验数据/道路txt/bay.txt"
    #dataExtractor(bay_file_path)
if __name__ == '__main__':
    main()
