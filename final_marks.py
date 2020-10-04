# @Author: two_0
# @Date:   04-10-2020
# @Email:  philip@two-0.org
# @Project: Python Tutorial
# @Last modified by:   two_0
# @Last modified time: 04-10-2020
# @Copyright: Copyright 2020 © - All Rights Reserved
#     ___ __ ._`.*.'_._ ____ רףאל
#    . +  * .\   o.* `.`. +.  א .
#   *  .ת' '  \^/|  `. * .  * `
#             \V/ . +
#    יהוה      /_\  .`.
#   ======== _/W\_ =אדני:By: Two.0:.*
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
if len(sys.argv) != 2:
    raise ValueError('Please provide file name.')
filename = sys.argv[1]
path = '/home/two_0/Downloads/'
full_path = path+filename
lines = []
with open(full_path, 'r') as file:
    lines = file.readlines()
score_list = []
#remove spaces in data
for item in lines:
    #seperating the data out
    scores = item.split(' ')
    #converting data into ints
    score_list += [int(x) for x in scores]
#converting to numpy array
x = np.array(score_list)
fig, ax = plt.subplots(figsize = (10,7))
ax.hist(x, bins = [0,10,20,30,40,50,60,70,80,90,100])
plt.show()
