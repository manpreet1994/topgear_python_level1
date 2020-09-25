#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:09:07 2020

@author: manpreet
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


q1list = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', 'www.website.org', 'www.bis.org.in', 'www.rbi.org.in']
print("1. Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]; Sort the list based on the top level domain (edu, com, org, in) using custom sorting")
print ("Input :", q1list)

print(q1(q1list))