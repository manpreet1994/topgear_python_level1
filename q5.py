#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:24:24 2020

@author: manpreet
"""


def q5(inputlist):
    final =  [inputlist[x] for x in range(0, len(inputlist)-1) if not inputlist[x]==inputlist[x+1]]
    final.append(inputlist[-1])
    return final



print("Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.")

#5.
print("input = [1, 2, 2, 3]","output = ",q5( [1, 2, 2, 3]))
print("input = [2, 2, 3, 3, 3]","output = ",q5[2, 2, 3, 3, 3])