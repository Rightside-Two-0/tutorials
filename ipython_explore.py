# @Author: two_0
# @Date:   23-09-2020
# @Email:  philip@two-0.org
# @Project: Python Tutorial
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
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#IPython in Atom text editor!
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import *
Image('https://ipython.org/_static/IPy_header.png')
#%%md
#Audio!
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
Audio(url="http://www.nch.com.au/acm/8k16bitpcm.wav")
#%%md
#Custom Sound
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
import numpy as np
max_time = 13
f1 = 220.0
f2 = 224.0
rate = 8000
L = 13
times = np.linspace(0,L,rate*L)
signal = np.sin(2*np.pi*f1*times) + np.sin(2*np.pi*f2*times)
Audio(data=signal, rate=rate)
#%%md
#YouTube Videos
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
YouTubeVideo('NI26dqhs2Rk')
#%%md
#HTML
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
page = '''
    <table>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
        <tr>
            <td>row 1, cell 1</td>
            <td>row 1, cell 2</td>
        </tr>
        <tr>
            <td>row 2, cell 1</td>
            <td>row 2, cell 2</td>
        </tr>
    </table>
'''
HTML(page)
#%%md
#Data Explorer
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
import pandas as pd
pd.options.display.html.table_schema = True
pd.options.display.max_rows = None
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df1 = pd.read_csv(iris_url)
df1
