import nltk


def getWordList(txt):
    skip = ['！','…','（','）','—','、','；','：','‘','’','“','”','，','。','《','》','？']  # 需要排除的标点符号
    ret = []
    for s in txt:
        if s not in skip:
            ret.append(s)
    return ret



def calcFreq(txt):
    wordList = getWordList(txt)
    return nltk.FreqDist(wordList)


if __name__ == "__main__":
    test = "这，是一个测试字符串。这，是另一个"
    print(calcFreq(test).most_common(10))
