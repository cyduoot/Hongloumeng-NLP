import singleFreq
import nltk
import random


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


def prepare(s):  # 将文章导入并标好是前80回还是后40回，分别用0,1表示
    ret = []
    for i in range(1, 121):
        fileName = "text\\chapter" + str(i) + ".txt"
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


if __name__ == "__main__":
    ac = {}
    ac[40] = 0
    ac[60] = 0
    ac[80] = 0
    for times in range(1, 101):
        print(times)
        for i in range(1, 4):
            # print(20 + i * 20)
            labeled_text = prepare(20 + i * 20)
            random.shuffle(labeled_text)
            count0 = 0  # 训练集使用的前80回计数器
            count1 = 0  # 训练集使用的后40回计数器
            train_set = []
            test_set = []
            for iter in labeled_text:  # 拆分训练集和测试集
                if iter[1] == 0:
                    if count0 < 20:
                        train_set.append((chapterFeatures(iter[0]), iter[1]))
                        count0 += 1
                    else:
                        test_set.append((chapterFeatures(iter[0]), iter[1]))
                else:
                    if count1 < 20:
                        train_set.append((chapterFeatures(iter[0]), iter[1]))
                        count1 += 1
                    else:
                        test_set.append((chapterFeatures(iter[0]), iter[1]))
            classifier = nltk.NaiveBayesClassifier.train(train_set)
            # print(nltk.classify.accuracy(classifier, test_set))
            ac[20 + i * 20] += nltk.classify.accuracy(classifier, test_set)
    ac[40] = ac[40] / 100
    ac[60] = ac[60] / 100
    ac[80] = ac[80] / 100
    print(ac)  # 计算并输出平均准确度
#    for s in saved:
#        print(classifier.classify(chapterFeatures(s[0])))
