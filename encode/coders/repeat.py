#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:10:33 2019

@author: maylibooyah69
"""

#print('hello world')

with open('../signal/spm.txt') as spm:
    msg=spm.read()
    
print(msg)

def str2bin(s):
    out=[]
    for i in s:
        asc=ord(i)
        bi=bin(asc)
        out.append(bi)
    return out

def bin2str(s):
    return "".join(chr(int(i,2)) for i in s)


def repcode(m,n):
    out=[]
    for i in m:
        for j in range(n):
            out.append(i)
    return out


binmsg=str2bin(msg)
repbinspm=repcode(binmsg,3)
binspm=bin2str(repbinspms)
print(binspm)
#repspm=bin2str(binspm)
#print(repspm)