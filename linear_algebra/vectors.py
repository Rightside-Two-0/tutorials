# @Author: two_0
# @Date:   26-09-2020
# @Email:  philip@two-0.org
# @Project: Python Tutorial
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
    plt.arrow(0,0,x,y,width=.08)
    plt.grid()
    plt.show()
#%%
#testing
vector(-12,2)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
IFrame('https://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_1/vectors_matrices_sympy.html', width=600, height=400)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
import math
math.sqrt(8)
sqrt(8)
#%%
2/7
Rational(2,7)
Rational(S(2), 7)
Float(2.5e-10)
Rational(.75)
Rational(.2)
Rational('0.2')
Rational(23e-10).limit_denominator(10**12)
S('.[1]')
oo
#%%
e
e
I
I*I
I-sqrt(-1)
pi
pi.is_irrational
#%%
Latex('$e^{i\pi}+1=0$')
(e**(I*pi)+1).evalf()
N(sqrt(2)*pi)
#%%
x, y = symbols('x,y')
f_x = Eq(y,x**2)
f_x
f2_x = y - x**2
f2_x
plot(x**2)
plot_implicit(f2_x)
#%%
f2_x
f2_x.subs(y,2)
f2_x.subs(y, x**3)
#%%
#solve
expr = 3*x+6
solveset(expr)
#%%
#solve linear system of equations
eq1 = Eq(3*x+4*y,6)
eq2 = Eq(5*x+3*y,7)
eqs = [eq1,eq2]

linsolve(eqs,(x,y))
#%%
#Calculus
exp_2 = 3*x**2
exp_2
d_exp_2 = exp_2.diff(x)
d_exp_2
d_exp_2.integrate(x)
#%%
M = Matrix(2,2,[1,0,0,1])
M
M = eye(2)
M
M = zeros(2,2)
M
M = eye(2)*2
M
minv = M**-1
minv
#%%
v = Matrix([1,1])
v
M*v
#%%
#symbols inside matrices
