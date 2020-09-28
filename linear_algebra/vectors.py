# @Author: two_0
# @Date:   26-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 28-09-2020
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
IFrame('https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html', width=600, height=400)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Algebraic & Geometric interpretations of Vectors
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
IFrame('https://i.stack.imgur.com/2Set2.png', width=600, height=400)
#%%
YouTubeVideo('fNk_zzaMoSs')
#%%
'''
A vector has two key characteristics, that of its angle &
its length.  It is possible to define any vector with only
these two things.  It is also possible to know the orientation
and simply use two numbers to represent the point in the plane
with the length extended to the origin.
'''
import matplotlib.pyplot as plt
def vector(x_coordinate, y_coordinate):
    plt.arrow(0, 0, x_coordinate, y_coordinate, width = 0.08)
    plt.grid()
    plt.show()
#%%
#testing
vector(-12,2)
#%%md
#Vector Addition & Subtraction
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
IFrame('https://www.qsstudy.com/wp-content/uploads/2017/03/Vectors-addition-and-subtraction.jpg', width=600, height=400)
#%%
import os
path = '/home/two_0/Downloads/linear_algebra_Udemy'
Video(path+'/2. Vectors/3. Vector addition and subtraction.mp4', embed=True, width=400, height=300)
#%%
'''
Adding a vector in a geometric way involves using the
'tip to tail' technique.  Subtraction is adding a negative.
The computation is to add x1 to x1 & y1 to y2.
'''
def add_vector(vector_1, vector_2):
    plt.arrow(0,0,vector_1[0], vector_1[1], width=0.08, color='red')
    plt.arrow(vector_1[0], vector_1[1],vector_2[0], vector_2[1], width=0.08, color='blue')
    resultant = [vector_1[0]+vector_2[0],vector_1[1]+vector_2[1]]
    plt.arrow(0,0,resultant[0], resultant[1], width = 0.08, color='green')
    plt.grid()
    plt.show()
#%%
#testing
v = [5,3]
w = [1,17]
add_vector(v,w)
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Vector Scalar Multiplication
#%%
IFrame('https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Compatibility_of_linear_map_with_scalar_multiplication_2.svg/800px-Compatibility_of_linear_map_with_scalar_multiplication_2.svg.png', width=600, height=400)
#%%
IFrame('https://4.bp.blogspot.com/_Ox-YAvoPntU/SPSwabSsqfI/AAAAAAAAAWs/cJU3ea83j8Y/s400/Matrix+and+Det+error.gif', width=600, height=400)
#%%
Video(path+'/2. Vectors/4. Vector-scalar multiplication.mp4', embed=True, width=400, height=300)
#%%
def scalar_multiply(scalar, vector):
    return [vector[0]*scalar, vector[1]*scalar]
#%%
#testing
scalar_multiply(3, [5,12])
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Vector Multiplication
#%%
IFrame('https://courses.eas.ualberta.ca/eas421/diagramspublic/equations/vectordotproduct.gif', width=600, height=400)
#%%
YouTubeVideo('LyGKycYT2v0')
#%%
'''
The dot product is the 1st type of vector Multiplication.
It takes two vectors and reduces them down to a single
number that we call a scalar.
'''
Latex('$[A_1,A_2,A_3]*[B_1,B_2,B_3] = \sum_{i=1}A_i*B_i$')
def dot_product(vector_1, vector_2):
    if len(vector_1) == len(vector_2):
        dot = 0
        for item in range(len(vector_1)):
            dot += vector_1[item]*vector_2[item]
        return dot
    return 'INVALID MUST BE SAME SIZES'
#%%
#testing
dot_product([3,4],[6,7])
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Vector Length
IFrame('', width=600, height=400)
#%%
YouTubeVideo('5ptH2Xw4DZc')
#%%
Latex('$||\overline{a}|| = \sqrt{x^2+y^2}$')
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Dot Product
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Outter Product
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Vecotr Cross-Product
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Vectors with Complex Numbers
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Conjugate Transpose
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Unit Vectors
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Dimensions & Fields
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Subpaces
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Subspaces vs Subsets
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Span
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Linear Independence
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Basis
IFrame('', width=600, height=400)
#%%
YouTubeVideo('')
#%%

#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
