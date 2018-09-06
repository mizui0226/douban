# -*- coding: utf-8 -*-
import json

with open('movie.json','r') as f:
    a = f.readlines()

s = ''
for i in a:
    s += i

str = json.dumps(s)
with open('movie1.json','w+') as fw:
    fw.write(str)
