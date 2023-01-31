# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:27:24 2023

@author: INDRA
"""

# Python program to print positive Numbers in a List

# list of numbers
list1 = [-10, 21, -4, -45, -66, 93]
num = 0

# using while loop	
while(num < len(list1)):
	
	# checking condition
	if list1[num] >= 0:
		print(list1[num], end = " ")
	
	# increment num
	num += 1
	
