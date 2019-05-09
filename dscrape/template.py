#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:57:44 2019

@author: maylibooyah69
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#params:
outputfile='scraped/agoodmovietowatch.csv'
quote_page = 'https://agoodmovietowatch.com/'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.findAll('span', attrs={'class': 'content-title'}) #tag pattern1
name_box2 = soup.findAll('a', attrs={'class': 'text-excerpt'}) #tag pattern2

temp=[]
for i in zip(name_box,name_box2):
    text="Title: "+i[0].text.strip() + "\nReview:" + i[1].text.strip()
    temp.append(text)
#print(temp[0])

with open(outputfile,'a') as csv_file:
    writer = csv.writer(csv_file)
    for i in zip(name_box,name_box2):
        t1="Title: "+i[0].text.strip()
        t2="Review:" + i[1].text.strip()
        writer.writerow([t1, t2,datetime.now()])
print("hehe")
