# -*- coding: utf8 -*-
# Convert cvc.txt into 3D array of [0,1]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
consonants = ['0', 'ph', 'p', 'b', 'm', 'th', 't', 'n', 'l', 'kh', 'k', 'g', 'ng', 'ch', 'chh', 'j', 's', 'h']

vowels = []

c_vals = []
v_vals = []
t_vals = []

xs = open('cvc.txt')
for l in xs:
    l = l.rstrip()
    c = l[:7].rstrip()
    v = l[7:14].rstrip()
    t = l[14:]

    if len(c) == 0:
        c = 0
    else:
        c = consonants.index(c)
    if v not in vowels:
        vowels.append(v)
    v = vowels.index(v)
    t = int(t)
    print('{},{},{},{}'.format(c, v, t, l.replace(' ', '')))
    # c_vals.append(c)
    # v_vals.append(v)
    # t_vals.append(t)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(c_vals, v_vals, t_vals, marker='s')
# ax.set_xlabel('Onset')
# ax.set_ylabel('Segment')
# ax.set_zlabel('Tone')
# pyplot.show()
