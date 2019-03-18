# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:10:46 2019

@author: S291366
"""
lista=[]
import numpy as np
import csv
import matplotlib.pyplot as plt

with open('dane.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    for wiersz in readCSV:
        
        i=wiersz[0]
        
        j=wiersz[7]
        if i=='y' or j=='pressure':
            pass
        else:
            if float(i)==2004:
                lista.append(float(j))
presure=np.array(lista)
for i in range(12):
    print(np.min(np.split(presure,12)[i]))
    print(np.max(np.split(presure,12)[i]))
    