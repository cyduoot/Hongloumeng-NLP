import singleFreq
import math


def chapterFeatures(text):  # 提取根据先验知识选取的虚词特征
    keyWords = ['之', '其', '或', '亦', '于', '即', '皆', '因', '仍', '故', '尚', '乃', '吗', '罢', '了', '的', '着',
                '一', '不', '把', '向', '是', '在', '可', '便', '但', '越', '比', '很', '偏']  # 所选取的作为特征的虚词
    feature = {}
    for c in keyWords:
        feature[c] = 0
    for line in text:
        tmp = singleFreq.getWordList(line)
        for s in tmp:
            if s in keyWords:
                feature[s] += 1  # 虚词计数
    return feature

if __name__ == "__main__":
    Feature = {}
    for i in range(0,3):
        Feature[i] = {}
        for j in range(i * 40 + 1, i * 40 + 40):  # 统计每个关键字出现的次数
            fileName = "./text/chapter" + str(j) + ".txt"
            f = open(fileName, encoding="utf-8")
            txt = []
            line = f.readline()  # 处理过后实际上一回只有一行
            cur = chapterFeatures(line)
            for item in cur:
                if item in Feature[i].keys():
                    Feature[i][item] += cur[item]
                else:
                    Feature[i][item] = cur[item]
        total = 0  # 计算关键字出现的概率
        for it in Feature[i]:
            total += Feature[i][it]
        for it in Feature[i]:
            Feature[i][it] = Feature[i][it] / total
    KL = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            for it in Feature[i]:
                KL[i][j] += Feature[i][it] * math.log(Feature[i][it]/Feature[j][it])
    print(KL)
