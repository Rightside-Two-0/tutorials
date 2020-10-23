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
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Sum of the 1st 'n' integers
def sum_to():
    up_to = int(input('Please provide an integer 100 or less'))
    total = 0
    for item in range(1, up_to+1):
        total += item
    return total
#%%
sum_to()
assert sum_to() == 100*101/2
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Widgets & gizmos
def get_total_weight():
    widget_weight = 75
    gizmo_weight = 112
    widget_number = int(input('Enter number of widgets sold:'))
    gizmo_number = int(input('Enter number of gizmos sold:'))
    return f'Total weight of the parts is: {(widget_number*widget_weight+gizmo_number*gizmo_weight)/1000} kilograms'
#%%
get_total_weight()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Arithmetic
def arithmetic():
    a = int(input('Enter a valid integer'))
    b = int(input('Enter a another valid integer'))
    sum_str = f'The sum of a and b is {a+b}\n'
    difference_str = f'The difference when b is subtracted from a is {a-b}\n'
    product_str = f'The product of a and b is {a*b}\n'
    quotient_str = f'The quotient when a is divided by b is {a//b}\n'
    remainder_str = f'The remainder when a is divided by b is {a%b}\n'
    result_log = f'The result of log_10(a) is {math.log10(a)}\n'
    result_exp = f'The result of a^b is {a**b}\n'
    return sum_str+difference_str+product_str+quotient_str+remainder_str+result_log+result_exp
#%%
print(arithmetic())
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Fuel efficiency
def get_conversion_rate():
    mpgs = int(input('Enter the US MPGs that was used:'))
    canada_eqv = (100*3.785411784)/(1.609344*mpgs)
    return '{0:,.2f}'.format(canada_eqv)
#%%
get_conversion_rate()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Distance between 2 points on Earth
#distance = 6371.01×arccos(sin(t1)×sin(t2)+cos(t1)×cos(t2)×cos(g1 − g2))
def get_distance():
    t1 = math.radians(float(input('Enter Latitude 1 as degrees')))
    g1 = math.radians(float(input('Enter Longitude 1 as degrees')))
    t2 = math.radians(float(input('Enter Latitude 2 as degrees')))
    g2 = math.radians(float(input('Enter Longitude 2 as degrees')))
    return 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
#%%
get_distance()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Making change
def get_change():
    cents = int(input('Enter the number of cents to be returned'))
    num_toonies = 0
    num_loonies = 0
    num_quaters = 0
    num_dimes = 0
    num_nickles = 0
    num_pennies = 0
    while cents > 0:
        update = 0
        if cents % 200 == 0:
            num_toonies += 1
            update = 200
        elif cents % 100 == 0:
            num_loonies += 1
            update = 100
        elif cents % 25 == 0:
            num_quaters += 1
            update = 25
        elif cents % 10 == 0:
            num_dimes += 1
            update = 10
        elif cents%5 ==0:
            num_nickles += 1
            update = 5
        elif cents%1 == 0:
            num_pennies += 1
            update = 1
        cents = cents-update
    return {'Toonies':num_toonies, \
            'Loonies':num_loonies, \
            'Quaters':num_quaters, \
            'Dimes':num_dimes, \
            'Nickles':num_nickles, \
            'Pennies':num_pennies}
#%%
get_change()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Height units
def convert_centi():
    feet = int(input('Please enter height in feet'))
    inches = int(input('please enter the height in inches'))
    return feet*12*2.54+inches*2.54
#%%
convert_centi()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Area and volume
def get_area_volume():
    radius = float(input('Enter the radius of your circle'))
    area = math.pi*radius*radius
    assert radius**2 == radius*radius
    volume = (4/3)*math.pi*radius*radius*radius
    return area, volume
#%%
get_area_volume()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Heat capicity
def get_head_capicity():
    mass = float(input('Enter the mass of the water'))
    temp_delta = float(input('Enter the temperature change'))
    energy = mass*4.186*temp_delta
    return energy
#%%
get_head_capicity()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Volume of cylinder
def get_cylinder_vol():
    radius = float(input('Enter the radius of bottom'))
    height = float(input('Enter the height'))
    result = (math.pi*radius*radius)*height
    return '{0:,.1f}'.format(round(result, 1))
#%%
get_cylinder_vol()
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% Free fall
