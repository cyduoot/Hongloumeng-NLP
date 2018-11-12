# -*- coding:utf-8 -*-

if __name__ == "__main__":

    f = open("./text/all.txt", encoding='utf-8')
    line = f.readline()
    chapterNum = 0
    chapter = []
    while line:
        if line[0] == "第":   # 由于精校版文本的特点，有且只有章节名的第一个字是“第”
            with open("./text/chapter" + str(chapterNum) + '.txt', "w", encoding='utf-8') as of:
                for L in chapter:
                    of.write(L)
                of.close()   # 一章的开始也是上一章的结束，故输出上一章内容
            chapterNum += 1
            chapter = []
        line = line.strip('\n')
        line = line.strip(' ')      # 去掉空行空格
        chapter.append(line)
        line = f.readline()
    with open("./text/chapter" + str(chapterNum) + '.txt', "w", encoding='utf-8') as of:
        for L in chapter:
            of.write(L)
        of.close()   # 输出最后一章内容
