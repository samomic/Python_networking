# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:01:24 2021

@author: Samir
"""

import numpy as np
# define matrix A using Numpy arrays
A = np.array([[0, 0.98, 0, 0, 0, 0, 0, 0, 0, 0.02],
              [0, 0, 0.1, 0.85, 0, 0, 0, 0, 0, 0.05],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0.6, 0.3, 0, 0, 0.1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0.5, 0, 0, 0, 0, 0.5, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0.3, 0.7, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, -1]]) 

#define matrix B
B = np.array([56, 0, 0, 0, 0, 0, 0, 0, 0, 0]) 

# linalg.solve is the function of NumPy to solve a system of linear scalar equations
print ("Solutions:\n",np.linalg.solve(A, B )) 