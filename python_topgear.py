#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:24:44 2020

@author: manpreet

Python Assignment

1. Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]; Sort the list based on the top level domain (edu, com, org, in) using custom sorting
2. Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  

['axa', 'xyz', 'gg', 'x', 'yyy']
['x', 'cd', 'cnc', 'kk']
['bab', 'ce', 'cba', 'syanora']

3. Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.  e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
Hint: this can be done by making 2 lists and sorting each of them before combining them.
['bbb', 'ccc', 'axx', 'xzz', 'xaa']
['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

4. Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 
e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
      Hint: use a custom key= function to extract the last element form each tuple.
 [(1, 3), (3, 2), (2, 1)]
[(1, 7), (1, 3), (3, 4, 5), (2, 2)]

5. Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
 [1, 2, 2, 3], [2, 2, 3, 3, 3]

6. Write a function to print the information in the dictionary(bookstore) in the given format

bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}


BOOKSTORE

'Learning XML', 'Erik T. Ray', '2003', '39.95' 
'Everyday Italian', 'Giada De Laurent is', '2005', '30.00']
 'Harry Potter', 'J K. Rowling', '2005', '29.99']

7. Given a string, str1= Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.
Build a dictionary, with "words as key" --> Frequency of occurrence as value
E.g. Python à7, isà3
Print the top 5 words with their frequency of occurrence

8. Given a string, str1=""”Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.
Hint:  Assume that the first word is preceded by " "
Build a dictionary where the key is a word and the value is the list of words that are likely to follow.
E.g. Python à [is, has, features, interpreters, code, Software]. In this example the words listed are likely to follow “Python”
Given a word predict the word that’s likely to follow.

9. Below is the output of # show ip interface brief command on a router

Interface  IP-Address OK?  Method Status Protocol
 
FastEthernet0/0 192.168.1.242 YES  manual up up 
FastEthernet1/0        unassigned YES  unset  down 
Serial2/0               192.168.1.250 YES  manual up up 
Serial3/0               192.168.1.233 YES  manual up up 
FastEthernet4/0        unassigned YES  unset    down 
FastEthernet5/0        unassigned YES        unset   down

Use regular expressions to extract and display Interface and method status for all the interfaces.
E.g.  FastEthernet0/0, manual up

10. Given a number line from -infinity to +infinity. You start at 0 and can go either to the left or to the right. The condition is that in i’th move, you take i steps. In the first move take 1 step, second move 2 steps and so on. 
Hint: 3 can be reached in 2 steps (0, 1) (1, 3). 2 can be reached in 3 steps (0, 1) (1,-1) (-1, 2)
a) Find the optimal number of steps to reach position 1000000000 and -1000000000. 

"""



def q1(inputlist):
	tempDomainList = ["edu","com","org","in"]
	tempUrlList = inputlist
	sortedUrlList = []
	
	for i,v in enumerate(tempDomainList):
		for i1,v1 in enumerate(tempUrlList):
			if v1.endswith(v):
				sortedUrlList.append(v1)

	return sortedUrlList


def q2(inputlist):
    count=0
    for x in inputlist:
        if len(x)>1 and (x[0] == x[-1]):
            count = count+1
            
    return count
    
def q3(inputlist):
    templist=[]
    
    for x in inputlist:
        if x[0].lower() == 'x':
            templist.append(x)
            inputlist.remove(x)
    
    templist.sort()
    inputlist.sort()
    
    return templist+inputlist
        
def q4_get_item(input_tuple):
    return input_tuple[-1]

def q4(inputlist):
     inputlist.sort(key=q4_get_item)
     return inputlist

def q5(inputlist):
    final =  [inputlist[x] for x in range(0, len(inputlist)-1) if not inputlist[x]==inputlist[x+1]]
    final.append(inputlist[-1])
    return final


def q6(inputdict):
    temp_list=[]
    for x in inputdict['New Arrivals'].keys():
        temp_list.append(bookstore['New Arrivals'][x])
    temp_list.sort(key = lambda x: x[2])
    [print(x) for x in temp_list]
    


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

def q8(inputstr):
	dic={}
	wordList=inputstr.split()
	length=len(wordList)
	for index,word in enumerate(wordList):
		if word in dic:
			continue
		tmpList=[]
		for i in range(index,length):
			if index==length-1:
				break
			if word==wordList[i]:
				nextWord=wordList[i+1]
				tmpList.append(nextWord)

		dic[word]=tmpList
	return dic

def q8_predict(inputstr,word):
	wordDictionary=q8(inputstr)
	print("in the given string, the word ' ",word,"' is likely followed by the list of words",wordDictionary[word])


def q9(inputstr):
    import re
    print ("\n\n\n")
    for line in inputstr.splitlines():
    
    	matchObj = re.match( r'(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+\w+', line, re.M|re.I)
    
    	if matchObj:
    	   print(matchObj.group(1),",",matchObj.group(2),"\n")
    print ("\n\n\n"	)


def q10(target) : 
  
    target = abs(target) 
    
    sum = 0
    step = 0
    while (sum < target or (sum - target) % 
                                  2 != 0) : 
        step = step + 1
        sum = sum + step 
      
    return step 

###################################### ########################################
#1. 

q1list = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', 'www.website.org', 'www.bis.org.in', 'www.rbi.org.in']
print(q1(q1list))

#2.
print(q1(['axa', 'xyz', 'gg', 'x', 'yyy']))

#3.

print(q2(['axa', 'xyz', 'gg', 'x', 'yyy']))
print(q2(['x', 'cd', 'cnc', 'kk']))
print(q2(['bab', 'ce', 'cba', 'syanora']))

#4.

print(q4([(1, 3), (3, 2), (2, 1)]))
print(q4([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

#5.
print(q5( [1, 2, 2, 3]))
print(q5([2, 2, 3, 3, 3]))

#6.
bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
print(q6(bookstore))

#7.
q7input = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."    
print(q7(q7input))

#8.
q7input = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."    
print(q8(q7input))

#9. 
q9str="""Interface		IP-Address	OK? 	Method Status	Protocol
 
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down"""

q9(q9str)

#10.

print(q10(1000000000))
print(q10(-1000000000))
      
  


        
    
    