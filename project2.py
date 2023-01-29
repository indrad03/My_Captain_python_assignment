# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:42:46 2023

@author: INDRA
"""
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
