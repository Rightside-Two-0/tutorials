# @Author: two_0
# @Date:   08-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 08-10-2020
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
#Get data for machine learning
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
from sympy import *
#%%
'''
Hello programmers, I am looking for help solving this problem.
The comparison is supposed to be case insensitive, so 'john' in new_users
should get rejected because 'John' is in current_users. I have experimented
with .lower() in a few places but get a syntax error every time.
Not sure what else to do. I appreciate any help.
'''
current_users = ['John','tom','richard','bob','steve']
new_users = ['john','charliebrown','bob','mark','tony']
for user in new_users:
    if user[0].upper()+user[1:] in current_users or user[0].lower()+user[1:] in current_users:
        print(f'Sorry {user}, you will need to enter a new username.')
    else:
        print(f'{user} is available!')
#%%
