# @Author: two_0
# @Date:   16-10-2020
# @Email:  philip@two-0.org
# @Project: Python Power Series
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
#Python Power
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
from sympy import *
import math
import matplotlib.pyplot as plt
#programming == Living Algebra
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
Image('/home/two_0/projects/tutorials/exercises/python.png')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
Image('/home/two_0/projects/tutorials/exercises/python.png', width=35, height=35)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
help(Image)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
YouTubeVideo('7bnzid1eV3g', start=300)
help(YouTubeVideo)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
help(Video)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
help(IFrame)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
help(HTML)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
help(Audio)
#%%md
#Hello Python Exercises!
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Mailing address
def get_address():
    name = 'Rightside Two_0'
    address = '4747 E 1st St'
    city = 'Tucson'
    state = 'AZ'
    zip_code = '85711'
    return name+'\n'+address+'\n'+city+', '+state+' '+zip_code
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
print(get_address())
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Hello user!
def hello_user():
    name = input('Enter name')
    return 'Hello '+name+'!\nIt is very nice to meet you!'
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
print(hello_user())
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Area of a room
def get_area_room():
    width = float(input('Enter width of room'))
    length = float(input('Enter length of room'))
    return width*length
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
get_area_room()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# get field aread given in feet but return in acres 43560
def get_field_area():
    width = float(input('Enter the width in feet'))
    length = float(input('Enter length in feet'))
    return (width*length)/43560
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
get_field_area()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Bottle deposit return <= 1L:.10 & > 1L:.25
def get_return():
    less_than = int(input('Enter less than or equal to 1 liter'))
    more_than = int(input('Enter more than 1 liter'))
    return '$'+'{0:,.2f}'.format(less_than*.1+more_than*.25)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
get_return()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# Tax & tip
def get_tax_tip():
    tax_rate = 0.0825
    tip_rate = 0.18
    cost_meal = float(input('Enter the cost of the meal'))
    tip_amount = tip_rate*cost_meal
    tax_amount = tax_rate*cost_meal
    total_cost_meal = cost_meal+tip_amount+tax_amount
    g = lambda var : '{0:,.2f}'.format(var)
    return f'Your tip amount is: {g(tip_amount)}\nYour tax amount is: {g(tax_amount)}\nYour total due is: {g(total_cost_meal)}'
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
print(get_tax_tip())
