import numpy as np

a = [1,2,3,4,5]

print('numpy array - > ', np.array(a))

print('numpy arange - > ', np.arange(1, 11, 1))

print('numpy arange (even) - > ', np.arange(1, 11, 2))

print('numpy 1D-zeros - > ', np.zeros(4))

print('numpy 2D-Zeros - > ', np.zeros((4, 3)))

print('numpy 1D-Ones - > ', np.ones(4))

print('numpy 2D-Ones - > ',np.ones((4, 3)))

print('numpy linspace - > ',np.linspace(1, 11, 10))

print('numpy eye for identity matrix - > ',np.eye(3))

print('numpy reshape - > ',np.arange(6).reshape(2, 3))

print('numpy random num - > ',np.random.rand(2, 3))

print('numpy normal random - > ',np.random.randn(2,3))

print('Matrix - > ',np.mat([2,3]))
