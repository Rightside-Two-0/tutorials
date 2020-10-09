# @Author: two_0
# @Date:   08-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 08-10-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#     ___ __ ._`.*.'_._ ____ רףאל
#    . +  * .\   o.* `.`. +.  א .
#   *  .ת' '  \^/|  `. * .  * `
#             \V/ . +
#    יהוה      /_\  .`.
#   ======== _/W\_ =אדני:By: Two.0:.*
def personal_independence(income, ave_expenses):
    if type(income) == type('PASSIVE'):
        return income > ave_expenses
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Get data for machine learning
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
from sympy import *
#%%
'''
100:90 --> Excellent
89:80 -> Very Good
79:65 --> Good
0:64 --> Poor
'''
def card_usage(input):
    if 90 <= input <= 100:
        return 'Excellent'
    elif 80 <= input <= 89:
        return 'Very Good'
    elif 65 <= input <= 79:
        return 'Good'
    else:
        return 'Poor'
#%%
#testing
card_usage(90)
