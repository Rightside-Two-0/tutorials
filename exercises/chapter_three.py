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
#programming == Living algebra
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
Image('/home/two_0/projects/tutorials/exercises/python.png')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
Image('/home/two_0/projects/tutorials/exercises/python.png', width=35, height=35)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
YouTubeVideo('7bnzid1eV3g', start=300)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Hello Python Exercises
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Mailing address
def get_address():
    name = 'Rightside Two_0'
    address = '4747 E 1st'
    city = 'Tucson'
    state = 'AZ'
    zip_code = '85711'
    return name+'\n'+address+'\n'+city+', '+state+' '+zip_code
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
print(get_address())
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
def hello_user():
    name = input('Please enter your name')
    return 'Hello '+name+', it is nice to meet you!'
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
hello_user()
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Area of a room
def get_room_area():
    width_room = float(input('Enter the width of room'))
    length_rooom = float(input('Enter the length of room'))
    return width_room*length_rooom
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
get_room_area()
assert get_room_area() == 13*42
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
