# -*- coding: utf8 -*-
# 把 Talmage.db 裡的 CV(C)T 結構抓出來，然後人工處理一些髒髒

import sqlite3
import re

db = sqlite3.connect('Talmage.db')
c = db.cursor()
c.execute('SELECT reading FROM words')

syllables = {}

for word in c.fetchall():
    syl = word[0].replace(' ', '-').split('-')
    for s in syl:
        s = re.sub('\(.+\)', '', s).replace(u'\ufeff', '').lower().strip()
        syllables[s] = syllables.get(s, 0) + 1

with open('syllables.txt', 'w', encoding='utf8') as f:
    for s in syllables.keys():
        f.write(s)
        f.write('\n')
        if not re.match(r'^[a-z0-8]+$', s):
            print(s)
