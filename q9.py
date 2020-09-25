#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:28:46 2020

@author: manpreet
"""

def q9(inputstr):
    import re
    print ("\n\n\n")
    for line in inputstr.splitlines():
    
    	matchObj = re.match( r'(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+\w+', line, re.M|re.I)
    
    	if matchObj:
    	   print(matchObj.group(1),",",matchObj.group(2),"\n")
    print ("\n\n\n"	)




q9str="""Interface		IP-Address	OK? 	Method Status	Protocol
 
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down"""

print ("input = ", q9str )

print("output = ", q9(q9str))
