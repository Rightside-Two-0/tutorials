# @Author: two_0
# @Date:   29-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
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
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
from sympy import *
init_printing()
a,b,c,d,e,f,g,h,i = symbols('a:i') # neat shorthand for multiple symbols!
IFrame('https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html', width=600, height=400)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
YouTubeVideo('kYB8IZa5AuE')
#%%
A = Matrix([[a,b,c],[d,e,f]])
A
A[1,0]
A[:,0],A[1,:]
A.rows
A.cols
A.shape
A.T
Matrix([a,b])
Matrix([[d,e]])
v_1 = Matrix([c, d])
v_1
v_2 = Matrix([e, f])
v_2
a*Matrix([c, d]) + b*Matrix([e, f])
v_1.T*v_2
v_1.dot(v_2)
v_1*v_2.T
v = Matrix([g,h,i])
A*v
#%%
import random
M = Matrix(4,4,[random.randint(0,16) for num in range(16)])
M
d = trace(M)
d
#%%
