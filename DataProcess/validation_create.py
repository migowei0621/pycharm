import os

def eachFile(filePath):
    pathDir = os.listdir(filePath)
    all_file = []
    for allfile in pathDir:
        eachf = os.path.join(filePath,allfile)
        all_file.append(eachf)
    return all_file


def check(all_data, validation_data):
    print(all_data[-500])
    print(validation_data[-500])


if __name__ == '__main__':

    filePath = "/Users/migowei/Documents/实验数据/30_padding/TraveltimeList"
    all_file = eachFile(filePath)

    # print(24*4*29) #2016年2月份作为验证集
    for f in all_file:
        fr = open(f,'r',encoding='utf-8')
        all_data = fr.read().split(' ')[0:-1]
        validation_data = all_data[-1:-2785:-1]
        validation_data = validation_data[-1:-2785:-1]
        fr.close()

        filew = "/Users/migowei/Documents/实验数据/30_padding/ValidationSet/" + f.split('/')[-1]
        fw = open(filew,'w')
        fw.write(str(validation_data))
        fw.close()