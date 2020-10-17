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
import math
import matplotlib.pyplot as plt
#Programming = Living algebra!
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#IPython
import os
path = os.getcwd()
path[:-10]
Image(path[:-10]+'tutorials/exercises/python.png')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('bY6m6_IIN94')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Hello Python!
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('KOdfpbnWLVo')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
print('Hello Python!')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('iAzShkKzpJo')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
message = 'Meet me tonight.'
message
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('_87ASgggEg0')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
a = 496
type(a)
a
print(a)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
e = 2.71828
type(e)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
z = 2 - 6.1j
type(z)
z.real
z.imag
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('Aj8FQRIHJSc')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
x = 28
y = 28.0
float(28)
3.14
int(3.14)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
x = 1.732
1.732+0j
complex(1.732)
float(1.732+0j)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
a = 2
b = 6.0
c = 12+0j
a+b
b-a
a*7
c/b
16/5
20/5
16%5
16//5
2/0
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('BVXv0-1Rcc8')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
help(__builtins__)
help(pow)
pow(2,10)
help(hex)
hex(10)
hex(12648430)
0xa
0xc0ffee
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
help('modules')
import math
dir(math)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
help(radians)
help(math.radians)
math.radians(180)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('9OK32jb_TdI')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
True
False
a = 3
b = 5
a == b
a != b
a > b
a < b
type(True)
type(False)
bool(28)
bool(-2.71828)
bool(0)
bool('Turing')
bool(' ')
bool('')
str(True)
str(False)
int(True)
int(False)
5+True
10*False
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('RjMbCUpvIgw')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
import datetime
dir(datetime)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
help(datetime.date)
gvr = datetime.date(1956,1,31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)
mill = datetime.date(2000,1,1)
dt = datetime.timedelta(100)
print(mill+dt)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
print(gvr.strftime('%A, %B %d, %Y'))
message = 'GVR was born on {:%A, %B %d, %Y}'
print(message.format(gvr))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
launch_date = datetime.date(2017,3,30)
launch_time = datetime.time(22,27,0)
launch_datetime = datetime.datetime(2017,3,30,22,27,0)
print(launch_date)
print(launch_time)
print(launch_datetime)
launch_time.hour
launch_time.minute
launch_time.second
launch_datetime.year
launch_datetime.month
launch_datetime.day
launch_datetime.hour
launch_datetime.minute
launch_datetime.second
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
now = datetime.datetime.today()
now.microsecond
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
moon_landing = '7/20/1969'
moon_landing_datetime = datetime.datetime.strptime(moon_landing, '%m/%d/%Y')
print(moon_landing_datetime)
type(moon_landing_datetime)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('f4KOjWS_KZs')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
