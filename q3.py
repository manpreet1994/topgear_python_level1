#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:18:57 2020

@author: manpreet
"""

def q3(inputlist):
    templist=[]
    
    for x in inputlist:
        if x[0].lower() == 'x':
            templist.append(x)
            inputlist.remove(x)
    
    templist.sort()
    inputlist.sort()
    
    return templist+inputlist



print("3. Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.  e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. ")

print("input ", "['bbb', 'ccc', 'axx', 'xzz', 'xaa']", " output = ", q3(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))

print("input ", "['mix', 'xyz', 'apple', 'xanadu', 'aardvark']", " output = ", q3(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

      
      