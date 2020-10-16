# @Author: two_0
# @Date:   16-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 16-10-2020
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
#Python Power!
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
from sympy import *
import math
import matplotlib.pyplot as plt
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#Reading user input
name = input('Please enter your name:')
name
#_ id(): returns the memory location as integer
id(name)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#_ ord() returns unicode value [0:65535]
#_ chr() returns the character value
ord('r')
id(ord('r'))
ord('1')
chr(65535)
chr(114)
chr(0)
print(chr(5))
print(chr(8))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
start = 65
for item in range(start, start+58):
    print(chr(item))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
for item_j in range(22+5):
    print(chr(item_j+1488))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#_ bin() returns the binary representation
bin(1)
bin(2)
bin(3)
bin(37710)
binary_num = bin(37710)
binary_num
id(binary_num)
bin(id(binary_num))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#_ int() returns the base 10 integer
int(binary_num, 2)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
greeting = 'Hello '+name[:1].upper()+name[1:]
greeting
res = ''.join(format(ord(i), 'b') for i in greeting)
res
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
