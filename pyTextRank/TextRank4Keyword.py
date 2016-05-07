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
import jieba

################################### PART2 CLASS && FUNCTION ###########################
input_str = "我今天看到他，   发现他心情不好，可   能是因为天气不好的缘故吧。"

def clean_str(input_str):
    cleaned_str = input_str.replace(" ", "")
    return cleaned_str

cleaned_str = clean_str(input_str)
split_str_generator = jieba.cut(cleaned_str)

def create_net():
    import networkx
    pass

for i in split_str_generator: print i

