# @Author: two_0
# @Date:   04-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 04-10-2020
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
#Validation Function
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Write a function named validate that takes code represented as a string
as its only parameter.

Your function should check a few things:

    the code must contain the def keyword
        otherwise return "missing def"
    the code must contain the : symbol
        otherwise return "missing :"
    the code must contain ( and ) for the parameter list
        otherwise return "missing paren"
    the code must not contain ()
        otherwise return "missing param"
    the code must contain four spaces for indentation
        otherwise return "missing indent"
    the code must contain validate
        otherwise return "wrong name"
    the code must contain a return statement
        otherwise return "missing return"

If all these conditions are satisfied, your code should return True.
'''
