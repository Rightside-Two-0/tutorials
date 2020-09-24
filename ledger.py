#%%
# @Author: two_0
# @Date:   23-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 23-09-2020
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
import pandas as pd
#Image, Audio, YouTubeVideo, HTML, IFrame
Image('/home/two_0/projects/tutorials/python.png')
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Ledger
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
path_file = '/home/two_0/projects/tutorials/Export.csv'
df.to_csv('ledger.csv', sep=',', encoding='utf-8', index='Date')
df_in = pd.read_csv(path_file)
df_in.head(25)
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
date = ''
from_account = ''
to_account = ''
amount = 0
notes = ''
inputs = [date,from_account,to_account,amount,notes]
for item in range(len(inputs)):
    inputs[item] = input()
df = pd.DataFrame([inputs], columns=['Date','From','To','Amount','Notes'])
df.head(15)
