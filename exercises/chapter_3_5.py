# @Author: two_0
# @Date:   18-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 18-10-2020
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
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Sum of the 1st 'n' integers
def sum_up_to():
    n = int(input('Enter a number less than 101'))
    id(n)
    total = 0
    for item in range(1, n+1):
        total += item
    return total
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
sum_up_to()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Widgets & gizmos
def get_total_weight():
    widget_weight = 75
    gizmo_weight = 112
    widget_number = int(input('Enter number of widgets sold: '))
    gizmo_number = int(input('Enter number of gizmos sold: '))
    return f'Total weight of the parts is: {(widget_number*widget_weight+gizmo_weight*gizmo_number)/1000}'
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
get_total_weight()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# arithmetic
def arithmetic():
    a = int(input('Enter a valid integer'))
    b = int(input('Enter a valid integer'))
    sum_str = f'The sum of a and b is {a+b}\n'
    difference_str = f'The difference when b is subtracted from a is {a-b}\n'
    product_str = f'The product of a and b is {a*b}\n'
    quotient_str = f'The quotient when a is divided by b is {a//b}\n'
    remainder_str = f'The remainder when a is divided by b is {a%b}\n'
    result_log = f'The result of log_10(a) is {math.log10(a)}\n'
    result_exp = f'The result of a^b is {a**b}\n'
    return sum_str+difference_str+product_str+quotient_str+remainder_str+result_log+result_exp
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
print(arithmetic())
a=42
b=13
a+b
a-b
a*b
a//b
a%b
math.log10(a)
a**b
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Fuel efficiency
def get_conversion_rate():
    #(100*3.785411784)/(1.609344*mpgs)
    mpgs = int(input('Enter the US MPGs that was used:'))
    canada_eqv = (100*3.785411784)/(1.609344*mpgs)
    return '{0:,.2f}'.format(canada_eqv)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
get_conversion_rate()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
