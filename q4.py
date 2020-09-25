#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:22:02 2020

@author: manpreet
"""

def q4_get_item(input_tuple):
    return input_tuple[-1]

def q4(inputlist):
     inputlist.sort(key=q4_get_item)
     return inputlist

print("4. Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]")

print("input = ", "[(1, 3), (3, 2), (2, 1)]" , "output = " , q4([(1, 3), (3, 2), (2, 1)]))
print("input = ", "[(1, 7), (1, 3), (3, 4, 5), (2, 2)]" , "output = ", q4([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))