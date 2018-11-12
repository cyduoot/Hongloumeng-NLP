import jieba
import random
from sklearn import svm
import numpy as np


def chapterFeatures(text):  # 提取根据先验知识选取的虚词特征
    keyWords = ['了', '的', '我', '道', '他', '说', '是', '也', '你', '又', '着', '来',
                '去', '不', '在', '便', '人', '有', '都', '叫', '就', '呢', '笑', '这',
                '那', '还', '要', '什么', '好', '听', '等', '一个', '见', '那里', '到',
                '儿', '和', '我们', '只', '上', '才', '给', '没有', '把', '倒', '个',
                '罢', '这里', '们', '问', '说道', '事', '如今', '听见', '你们', '看',
                '不知', '姑娘', '做', '走', '怎么', '出来', '他们', '不是', '奶奶', '老爷',
                '将', '一面', '起来', '知道', '得', '再', '拿', '吃', '因', '就是', '没', '忙',
                '请', '这个', '只见']  # 所选取的作为特征的虚词
    feature = {}
    for c in keyWords:
        feature[c] = 0
    for line in text:
        tmp = jieba.cut(line)
        for s in tmp:
            if s in keyWords:
                feature[s] += 1  # 虚词计数
    vectorX = []
    for item in feature:
        vectorX.append(feature[item])
    return vectorX


def prepare(s):  # 将文章导入并标好是前80回还是后40回，分别用0,1表示
    ret = []
    for i in range(1, 121):
        fileName = "./text/chapter" + str(i) + ".txt"
        f = open(fileName, encoding="utf-8")
        txt = []
        line = f.readline()
        while line:
            txt.append(line)
            line = f.readline()
        if i <= s:
            ret.append((txt, 0))
        else:
            ret.append((txt, 1))
    return ret

def test_accuracy(start = 80, end = 80, step = 1, trainSize = 20):
    if (start > end) or (step > 0 and ((end - start) % step > 0)):
        return NULL
    steps = (end - start) // step + 1
    ac = {}
    cur = start
    while cur <= end:
        ac[cur] = 0
        cur += step
    for times in range(1, 101):
        print(times)
        for i in range(0, steps):
            labeled_text = prepare(start + i * step)
            random.shuffle(labeled_text)
            count0 = 0  # 训练集使用的前80回计数器
            count1 = 0  # 训练集使用的后80回计数器
            train_setX = []
            train_sety = []
            test_setX = []
            test_sety = []
            for iter in labeled_text:  # 拆分训练集和测试集
                if iter[1] == 0:
                    if count0 < trainSize:
                        train_setX.append(chapterFeatures(iter[0]))
                        train_sety.append(iter[1])
                        count0 += 1
                    else:
                        test_setX.append(chapterFeatures(iter[0]))
                        test_sety.append(iter[1])
                else:
                    if count1 < trainSize:
                        train_setX.append(chapterFeatures(iter[0]))
                        train_sety.append(iter[1])
                        count1 += 1
                    else:
                        test_setX.append(chapterFeatures(iter[0]))
                        test_sety.append(iter[1])
            clf = svm.LinearSVC()  # 使用线性核函数
            clf.fit(train_setX, train_sety)  # 训练模型
            predict = clf.predict(test_setX)
            L = len(test_sety)
            numCorrect = 0
            for j in range(0, L):
                if test_sety[j] == predict[j]:
                    numCorrect += 1
            #  print(numCorrect/L)
            ac[start + i * step] += numCorrect/L
    cur = start
    while cur <= end:
        ac[cur] /= 100
        cur += step
    return ac  # 计算并返回平均准确度


if __name__ == "__main__":
    # 第一次测试
    # print(test_accuracy(start=40, end = 80, step = 20))
    # 第二次测试
    print(test_accuracy(start = 20, end = 100, step = 10, trainSize = 10))
