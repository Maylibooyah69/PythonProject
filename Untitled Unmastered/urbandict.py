#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:43:04 2019

@author: maylibooyah69
"""

import requests 
import sys
import json

url='http://api.urbandictionary.com/v0/define?'
pa={'term':sys.argv[1]}
got=requests.get(url,params=pa)
get=got.json()
defs=[x['definition'] for x in get['list']]
print(defs[0])