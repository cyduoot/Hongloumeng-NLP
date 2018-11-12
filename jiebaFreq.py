import jieba
import nltk

def calcFreq():
    temp = ''
    fileName = "./jiebasample.txt"
    f = open(fileName, encoding="utf-8")
    line = f.readline()
    while line:
        temp += line
        line = f.readline()
    text = jieba.cut(temp)
    fd = nltk.FreqDist(text)
    return fd

if __name__ == "__main__":
    fd = calcFreq()
    print(fd.most_common(100))