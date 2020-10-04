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
'''
Metropole
Bloemfontein
Cape Town
Durban
East London
Ekurhuleni
Johannesburg
Port Elizabeth
Pretoria
#1996
61
87
74
47
75
85
71
77
#2011
91
94
90
81
82
91
90
89
'''
import matplotlib.pyplot as plt
import numpy as np
def plot_electric():
    labels = ['BFN','CTN','DBN','ELN','GER','JHB','PEZ','PTA']
    year_1 = [61,87,74,47,75,85,71,77]
    year_2 = [91,94,90,81,82,91,90,89]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, year_1, width, label='1996')
    rects2 = ax.bar(x + width/2, year_2, width, label='2011')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Electricity')
    ax.set_title('Electricity by City')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc='upper right')
    plt.show()

plot_electric()
