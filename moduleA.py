#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:45:46 2017

@author: biyichen
"""

def get_text(file_name):
    
    text = {}
    try:
        with open(file_name) as fileinput:
            text = fileinput.read()
    except IOError as error:
        print(str(error))
    return text


def process_data(text_data):
    
    letters = 'abcdefghijklmnopqrstvuwxyz'
    data = {}
    for char in text_data:
        ch = char.lower()
        if ch in letters:
            if ch not in data:
                data[ch] = 1
            else:
                data[ch] += 1
    return data

def print_output(data_dictionary):
    
    print("{0:6s}{1:>5s}".format("char", "Count"))
    for char in data_dictionary:
        print("{0:s}{1:>8d}".format(char, data_dictionary[char]))
