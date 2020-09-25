#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:11:15 2020

@author: manpreet
"""


def q2(inputlist):
    count=0
    for x in inputlist:
        if len(x)>1 and (x[0] == x[-1]):
            count = count+1
            
    return count

print("2. Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.")


print("input ", "['axa', 'xyz', 'gg', 'x', 'yyy']" , q2(['axa', 'xyz', 'gg', 'x', 'yyy']))
print("input ", "['x', 'cd', 'cnc', 'kk']" , q2(['x', 'cd', 'cnc', 'kk']))
print("input ", "['bab', 'ce', 'cba', 'syanora']" , q2(['bab', 'ce', 'cba', 'syanora']))
