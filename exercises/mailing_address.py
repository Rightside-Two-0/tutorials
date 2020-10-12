# @Author: two_0
# @Date:   10-10-2020
# @Email:  philip@two-0.org
# @Project: Python Power Series
# @Last modified by:   two_0
# @Last modified time: 11-10-2020
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
#Programming = LIving algebra!
x, y =  symbols('x y')
eq1 = Eq(x**2+1)
eq1
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
solution = solve(eq1)
solution
-1 == I**2
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
eq1.subs(x,I)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
3 + math.sqrt(3)
3+sqrt(3)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
N(3+sqrt(3))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
3+sqrt(3) == 3+math.sqrt(3)
type(N(3+sqrt(3)))
type(math.sqrt(3)+3)
'''even though they give the exact same
value they are of different types and
therefore are not equal'''
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#Graph
plot(x**2+1)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(sin(x), (x, -pi, pi), line_color='red')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
from sympy.plotting import plot3d_parametric_line
plot3d_parametric_line(cos(x), sin(x), x, (x, -5, 5))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
sqrt(x)*sin(x)
plot(sqrt(x)*sin(x))
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(x)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(-x)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(x+7)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(x-7)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(3*x)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
plot(x/3)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%
#reading user input
name = input()
name
#_ id(): returns the memory location integer
id(name)
name = input('What is your name?')
#notice that it is the same location
id(name)
id(x)
#_ ord(): returns the unicode value [0:65535]
ord('r')
id(ord('r'))
ord('1')
chr(65535)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
start = 65
for item in range(start,start+26):
    print(chr(item))
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
for item_j in range(22+5):
    print(chr(item_j+1488))
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#_ bin(): returns the binary representation
bin(1)
bin(110)
bin(37710)
binary_number = bin(37710)
id(binary_number)
id(bin(37710))
id(bin(37710))
bin(id(bin(37710)))
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#_ int(): returns the base 10 integer
int(binary_number, 2)
