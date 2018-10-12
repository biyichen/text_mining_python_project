#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:21:37 2017

@author: biyichen
"""

def get_text(file_name):
    
    text = ''
    try:
        with open(file_name) as f:
            for line in f:
                text += line.strip() + " "
    except IOError as error:
        print(str(error))
    return text


def process_data(text_data):
    
    data = {}
    for word in text_data.split(" "):
        allword = word.lower()
        if allword not in data:
            data[allword] = 1
        else:
            data[allword] += 1
    return data


def print_output(data_dictionary):
    
    length = 0
    for key in data_dictionary:

        if len(key.strip()) > length:
            length = len(key)
    
    print("word".ljust(length), "count")
    for char in data_dictionary:
        if len(char.strip()) > 0:
            # final_str="{0:>{width}s}{1:>8d}".format(char, data_dictionary[char],width=str(length))
            print(char.ljust(length), data_dictionary[char])
