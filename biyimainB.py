#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:22:48 2017

@author: biyichen
"""

from moduleB import get_text, process_data, print_output

if __name__ == '__main__':
    file1 = "script01.txt"
    file2 = "script02.txt"
    # character count  moduleB
    text1 = get_text(file1)
    text2 = get_text(file2)
    data_dict = process_data(text1+text2)
    print_output(data_dict)