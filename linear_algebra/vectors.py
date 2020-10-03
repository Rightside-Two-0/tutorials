# @Author: two_0
# @Date:   26-09-2020
# @Email:  philip@two-0.org
# @Project: Python Tutorial
# @Last modified by:   two_0
# @Last modified time: 01-10-2020
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
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
from sympy import *
init_printing()
a,b,c,d,e,f,g,h,i = symbols('a:i')
IFrame('https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html',width=600, height=400)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Vectors
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
YouTubeVideo('fNk_zzaMoSs')
#%%
'''
A vector is a speacial matrix.  It has two key
characteristics, that of its angle and its
length or magnitude.
'''
import matplotlib.pyplot as plt
def vector(x,y):
    plt.arrow(0,0,int(x),int(y),width=.08)
    plt.grid()
    plt.show()
#%%
#testing
vector(-12,2)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
IFrame('https://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_1/vectors_matrices_sympy.html', width=600, height=400)
#%%md
#A vecotr is a speacil matrix with only 1 dimension
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
M = Matrix([[11,-2]])
M
#%%
M[0]
M[1]
type(int(M[0]))
vector(M[0], M[1])
