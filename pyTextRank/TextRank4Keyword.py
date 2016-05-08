# -*- coding: utf-8 -*-
# !/usr/bin/python
################################### PART0 DESCRIPTION #################################
# Filename: TextRank4Keyword.py
# Description:
#


# Author: Shuai Yuan
# E-mail: ysh329@sina.com
# Create:　2016-05-06 09:07:46
# Last:
__author__ = 'yuens'

################################### PART1 IMPORT ######################################


################################### PART2 CLASS && FUNCTION ###########################

def load_data(doc_dir=None):
    if doc_dir:
        with open(doc_dir, 'rb') as f:
            doc_str = f.read()
    else:
        doc_str = "我今天看到他，   发现他心情不好，可   能是因为天气不好的缘故吧。"
    return doc_str

# 去除特函数符号（空格）
def clean_str(input_str):
    cleaned_str = input_str.replace(" ", "")
    return cleaned_str

def word_segment(input_str):
    import jieba
    jieba.enable_parallel(4)
    import jieba.posseg as pseg
    word_generator = pseg.cut(input_str)
    return word_generator

# 去停用词，除形容词，副词
def undecorate(input_generator, stopword_dir=None):
    if isinstance(stopword_dir, str):
        with open(stopword_dir, 'rb') as f:
            stopword_str_list = map(lambda line: line.strip().decode("utf8"), f.readlines())
        #print len(stopword_str_list), stopword_str_list
        #print stopword_str_list[len(stopword_str_list)-1], type(stopword_str_list[len(stopword_str_list)-1])
        word_t_list = filter(lambda t: (t.word not in stopword_str_list) and (t.flag != 'a' and t.flag != 'd'),\
                             input_generator)
        #print word_t_list[0].word
        #print type(word_t_list[0].word)
    else:
        word_t_list = filter(lambda t: t.flag != 'a' and t.flag != 'd',\
                             input_generator)
    word_list = map(lambda t: t.word, word_t_list)
    return word_list

def get_window_2d_list(word_list, split_stopword_dir=None):
    if isinstance(split_stopword_dir, str):
        with open(split_stopword_dir, "rb") as f:
            split_stopword_str_list = map(lambda line: line.strip().decode("utf8"), f.readlines())
    else:
        pass


def create_net():
    import networkx
    pass

def text_rank():
    pass

################################### PART３ TEST #######################################

doc_dir = None
stopword_dir = "../data/input/stopword_without_split.txt"

input_str = load_data(doc_dir)
cleaned_str = clean_str(input_str)
word_tuple_generator = word_segment(cleaned_str)
word_list = undecorate(word_tuple_generator, stopword_dir)

print "".join(word_list)
print type(word_list)
print word_list


split_stopword_dir = "../data/input/split_stopword.txt"