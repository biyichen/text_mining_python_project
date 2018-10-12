#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 04:21:43 2017

@author: biyichen
"""
from collections import Counter
import re


def get_text(text_file):
    '''
    read in file and remove all non english words and numbers
    split to list of words
    '''
    with open(text_file, 'r') as f:
        line = f.read().lower()
        line = re.sub(r"[^a-zA-Z \n]+", "", line)
        word_list = line.split()
    return word_list


def process_data(word_list, stop_word=None):
    '''
    count words frequency 
    supporting both with stop word filter or without 
    return top 10 words with count
    '''
    filter_word = []
    if stop_word:
        filter_word = stop_word
    c = Counter()
    for d in word_list:
        if d not in filter_word:
            c[d] += 1

    return dict(c.most_common(10))


def print_output(data_dictionary1, data_dictionary2):
    # get all words that will appear in the output
    words = []
    for i in [data_dictionary1, data_dictionary2]:
        words += list(i.keys())
    # fix column width
    max_length = 10
    # print header
    print('{1:{0}s}{2:{0}s}{3:{0}s}'.format(
        max_length, 'WORD', 'Count 1', 'Count 2'))
    # print line seperator
    print('-' * max_length * 3)
    # loop over words and check if it exists in both side and fill 0 if not.
    for i in words:
        print('{1:{0}s}'.format(max_length - 1, i), end=' ')
        if i in data_dictionary1:
            c = data_dictionary1[i]
        else:
            c = 0
        print('{1:{0}d}'.format(max_length - 1, c), end=' ')
        if i in data_dictionary2:
            c = data_dictionary2[i]
        else:
            c = 0
        print('{1:{0}d}'.format(max_length, c))
