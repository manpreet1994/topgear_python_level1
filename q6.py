#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:26:38 2020

@author: manpreet
"""


def q6(inputdict):
    temp_list=[]
    for x in inputdict['New Arrivals'].keys():
        temp_list.append(inputdict['New Arrivals'][x])
    temp_list.sort(key = lambda x: x[2])
    [print(x) for x in temp_list]
    
    
    

bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}

print("input dictionary", bookstore)
print("output = " q6(bookstore))
