import numpy as np

a = [1,2,3,4,5]

print('numpy array - > ', np.array(a))                              # creates array

print('numpy arange - > ', np.arange(1, 11, 1))                     # creates consicutive numbered Array

print('numpy arange (difference of 2) - > ', np.arange(1, 11, 2))   # creates array with alternate numbers

print('numpy arange (difference of 3) - > ', np.arange(1,11,3))     # creates array with numbers having difference between each other 3

print('numpy 1D-zeros - > ', np.zeros(4))                           # creates 1-D array of 4 zeros

print('numpy 2D-Zeros - > ', np.zeros((4, 3)))                      # creates 2-D array of zeros of shape 4x3

print('numpy 1D-Ones - > ', np.ones(4))                             # create 1-D array of ones

print('numpy 2D-Ones - > ',np.ones((4, 3)))                         # create 2-D array of ones of shape 4x3

print('numpy linspace - > ',np.linspace(1, 11, 10))                 # Divide 1 to 11 with 10 equal parts

print('numpy eye for identity matrix - > ',np.eye(3))               # Identity Matrix

print('numpy reshape - > ',np.arange(6).reshape(2, 3))              # creates shape of 2x3 matrix from a range of 6 numbers

print('numpy random num - > ',np.random.rand(2, 3))

print('numpy normal random - > ',np.random.randn(2,3))

print('Matrix - > ',np.mat([[2,3],[3,2]]))
