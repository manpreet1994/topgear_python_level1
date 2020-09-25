#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:31:01 2020

@author: manpreet
"""

def q10(target) : 
  
    target = abs(target) 
    
    sum = 0
    step = 0
    while (sum < target or (sum - target) % 
                                  2 != 0) : 
        step = step + 1
        sum = sum + step 
      
    return step 


print("input = 1000000000", "output = ", q10(1000000000))

print("input = -1000000000", "output = ", q10(-1000000000))

      