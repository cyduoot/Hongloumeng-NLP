import singleFreq

if __name__ == "__main__":
    allDist = {}
    for i in range(1, 121):
        fileName = "./text/chapter" + str(i) + ".txt"
        f = open(fileName, encoding="utf-8")
        line = f.readline()
        while line:
            temp = singleFreq.calcFreq(line)
            for localkey in temp.keys():  # 所有词频合并。 如果存在词频相加，否则添加
                if localkey in allDist.keys():  # 检查当前词频是否在字典中存在
                    allDist[localkey] = allDist[localkey] + temp[localkey]  # 如果存在，将词频累加，并更新字典值
                else:  # 如果字典中不存在
                    allDist[localkey] = temp[localkey]  # 将当前词频添加到字典中
            line = f.readline()
    print(sorted(allDist.items(), key=lambda x: x[1], reverse=True))
