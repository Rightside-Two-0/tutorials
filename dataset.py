# @Author: two_0
# @Date:   07-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 07-10-2020
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
IFrame('https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset', width=600,height=400)
#%%
from matplotlib import pyplot as plt
import pandas as pd
# Enable the table_schema option in pandas,
# data-explorer makes this snippet available with the `dx` prefix:
pd.options.display.html.table_schema = True
pd.options.display.max_rows = 150
import os
#%%
df = pd.read_csv('/home/two_0/projects/tutorials/day.csv')
df.shape
df.columns
#%%
df
#%%
#total count(sales) as a function of temp
plt.scatter(df['temp'],df['cnt'])
#%%
pip install sklearn
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(df['temp'].values.reshape(-1,1),df['cnt'].values.reshape(-1,1))
lm.intercept_
lm.coef_
#%%
plt.scatter(df['hum'],df['cnt'])
