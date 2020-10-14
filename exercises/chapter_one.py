# @Author: two_0
# @Date:   10-10-2020
# @Email:  philip@two-0.org
# @Project: Python Power Series
# @Last modified by:   two_0
# @Last modified time: 13-10-2020
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
eq1 = Eq(x**2+1, 0)
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
#LateX
Latex('$3 + \sqrt{3}='+str((3+math.sqrt(3)))+'$')
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
chr(0)
print(chr(5))
print(chr(8))
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
binary_number
id(binary_number)
id(bin(37710))
id(bin(37710))
bin(id(bin(37710)))
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#_ int(): returns the base 10 integer
int(binary_number, 2)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
greeting = 'Hello ' + name[0:1].upper()+name[1:]
greeting
res = ''.join(format(ord(i), 'b') for i in greeting)
res
#%%md
##Exercises
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#mailing address
print('4747 E 1st\nTucson, AZ 85711')
street = '4747 E 1st'
city_state = 'Tucson, AZ 85711'
print(street+'\n'+city_state)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Hello+
name = input('What is your name?')
print('Hello '+name)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Area of room
width = float(input('Enter width(feet):'))
length = float(input('Enter length(feet):'))
area = width*length
print(f'The area of your room is {area} feet square.')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Area of a Field
width = float(input('Enter width(feet):'))
length = float(input('Enter length(feet):'))
area_feet = width*length
print(f'The area of your field is {round(area_feet/43560, 2)} acre.')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Bottle deposit
small_deposit = 0.1
big_deposit = .25
small = int(input('How many bottles less than or equal to 1 liter?'))
big = int(input('How many bottles greater than 1 liter?'))
refund = '{0:,.2f}'.format(small_deposit*small+big_deposit*big)
print(f'Your refund will be ${refund}')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Tax & Tip
cost = float(input('What was the cost of your meal?'))
tax = .08
tip = .18
tax_amount = '{0:,.2f}'.format(tax*cost)
tip_amount = '{0:,.2f}'.format(cost*tax)
total = '{0:,.2f}'.format(cost+tip+tax)
print(f'Thank you, your tax was ${tax_amount} and your tip was ${tip_amount}\nmaking your grand total ${total}')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Sum of the 1st n integers
n, summed = symbols('n sum')
number = int(input('Enter a positive integer'))
total = Eq((n*(n+1))/2, summed)
total
print(f'The sum up to your number {number} is {str(int((number*(number+1))/2))}')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Widgets & Gizmos
widget_weight = 75
gizmo_weight = 112
widgets = int(input('How many widgets were sold?'))
gizmos =  int(input('How many gizmos were sold?'))
total_weight = '{0:,.2f}'.format((widgets*widget_weight+gizmos*gizmo_weight)/1000)
print(f'The total weight of the parts to be shipped are {total_weight} kilograms')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Compound Interest
