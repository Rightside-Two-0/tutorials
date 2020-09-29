# @Author: two_0
# @Date:   26-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 29-09-2020
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
from IPython.display import *
from sympy import *
init_printing()
a,b,c,d,e,f,g,h,i = symbols('a:i') # neat shorthand for multiple symbols!
IFrame('https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html', width=600, height=400)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Algebraic & Geometric interpretations of Vectors
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
YouTubeVideo('fNk_zzaMoSs')
#%%
'''
A vector has two key characteristics, that of its angle &
its length.  It is possible to define any vector with only
these two things.  It is also possible to know the orientation
and simply use two numbers to represent the point in the plane
with the length extended to the origin.
'''
import matplotlib.pyplot as plt
def vector(x_coordinate, y_coordinate):
    plt.arrow(0, 0, x_coordinate, y_coordinate, width = 0.08)
    plt.grid()
    plt.show()
#%%
#testing
vector(-12,2)
#%%
IFrame('https://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_1/vectors_matrices_sympy.html', width=600, height=400)
#%%
2/7
Rational(2,7)
Rational(S(2),7)
Float(2.5e-10)
Rational(.75)
Rational(.2)
Rational('0.2')
Rational(23e-10).limit_denominator(10**12)
S('0.[1]')
oo

import math
math.sqrt(8)
#sympy
sqrt(8)
e
#%%
pi
#%%
I
I*I
I-sqrt(-1)
pi.is_irrational
#%%
