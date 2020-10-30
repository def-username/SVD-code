#!/usr/bin/env python
# coding: utf-8

# In[10]:


from numpy import array
import math 
from scipy.linalg import svd
import numpy as np
# define a matrix
A = array([[-math.cos(45*3.14/180),math.cos(45*3.14/180),math.cos(45*3.14/180),-math.cos(45*3.14/180)], 
           [math.sin(45*3.14/180),math.sin(45*3.14/180),math.sin(45*3.14/180),math.sin(45*3.14/180)], 
           [1,-1,1,-1]])
print(A)

U, s, VT = svd(A)

print("U matrix = ")
print(U)

print("S matrix = ")
print(s)

print("VT matrix = ")
print(VT)

new_s=np.array([[.5,0,0],[0,1/1.4,0],[0,0,1/1.4],[0,0,0]])
x=np.matmul(VT.transpose(),new_s)
y=np.matmul(x,U.transpose())

print(y)
forces = np.array([[0],[50],[0]])
Final=np.matmul(y,forces)
print(Final)


# In[ ]:




