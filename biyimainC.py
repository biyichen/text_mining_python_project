#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 04:20:15 2017

@author: biyichen
"""

from biyimoduleC import get_text, process_data, print_output
if __name__ == '__main__':
    file1 = "script01.txt"
    file2 = "script02.txt"
    stopwords = "stopwords.csv"
    # character count  moduleB
    text1 = get_text(file1)
    text2 = get_text(file2)
    stop_word = get_text(stopwords)
    output1 = process_data(text1, stop_word=None)
    output2 = process_data(text2, stop_word=stop_word)
    # print_output(data_dict)
    print_output(output1, output2)
