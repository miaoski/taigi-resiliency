# -*- coding: utf8 -*-
# 把洗乾淨的資料分出 CVCT

import re

re_c = re.compile(r'^[bcfghjklmnprsty]+')
re_t = re.compile(r'[2-8]$')
re_ng = re.compile(r'[aeiou]*ng[2-8]?')

consonants = {}
coda = {}

xs = open('syllables.txt').read().split('\n')
for x in xs:
    if len(x) == 0:
        continue
    ng = re_ng.search(x)
    if ng and ng.start(0) > 0:
        p = ng.start(0)
        c = x[:p]
        v = x[p:]
    elif x.startswith('hm'):
        c = 'h'
        v = x[1:]
    else:
        cons = re_c.search(x)
        if cons:
            p = cons.end(0)
            c = x[:p]
            v = x[p:]
        else:
            c = ''
            v = x
    t = re_t.search(v)
    if t:
        v = v[:-1]
        t = t[0]
    else:
        t = '1'
    print('{:5}  {:5}  {}'.format(c, v, t))
