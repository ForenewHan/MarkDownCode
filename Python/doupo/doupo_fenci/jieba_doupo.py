################################
#把斗破苍穹用jieba分词，并写入文件#
################################
import jieba

# 定义阻止词库
STOPWORDS = []

# 添加阻止词库
fp = open("HIT.txt","r")
for i in fp.readlines():
    STOPWORDS.append(i.strip())
fp.close()

fp = open("stop.txt","r")
for i in fp.readlines():
    STOPWORDS.append(i.strip())
fp.close()

# 读取name.txt以及others.txt中的特殊人名，并放到special_names里，之后加到jieba词库里
f_name = open("name.txt","r")
special_names = [name.strip() for name in f_name.readlines()]
for i in special_names:
    jieba.add_word(i)
f_name.close()

f_name = open("others.txt","r")
special_names = [name.strip() for name in f_name.readlines()]
for i in special_names:
    jieba.add_word(i)
f_name.close()

# 以上内容相当于预处理，下面内容开始分词
# 分词并把结果写入文件里
fp = open("doupo.txt", "r")
fsort = open("words_list.txt","w")
# 按照行来统计
for line in fp.readlines():
    clean_line = line.strip()
    # 每行都做一个jieba的分词，这里用默认模式，也就是精准分词
    word_list = jieba.cut(clean_line)
    # 对于分的词，如果不在STOPWORDS里，就写入文件
    for word in word_list:
        if word not in STOPWORDS:
            fsort.writelines(str(word) + '\n')
fp.close()
fsort.close()

print("jieba cut is finished\n")
