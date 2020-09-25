#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:28:16 2020

@author: manpreet
"""

def q7(inputstr): 
    
    inputstr.replace(",","")
    inputstr.replace(".","")
    inputstr.replace(")","")
    inputstr.replace("(","")
     
    inputlist =  inputstr.split(" ")
    freq = {} 
    for items in inputlist:
        freq[items] = inputlist.count(items) 
    
    return freq

q7input = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."    

print("input =", q7input)
print("output = ", q7(q7input))

print("top five words with frequency=", sorted(q7(q7input).items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:5])  


