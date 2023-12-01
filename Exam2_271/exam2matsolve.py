# When complete, this Python program will solve a linear
# Algebraic system of three equations for three unknows.

import numpy as np

matr=  np.array([[2,2,-1],[1,7,-3],[-2,-2,8]])#  COMPLETE THIS TO DEFINE YOUR MATRIX

rhs=  np.array([0,-2,6]) #  COMPLETE THIS TO ENTER YOUR RHS VECTOR

xvec= np.linalg.solve(matr,rhs) #  COMPLETE THIS STEP WITH THE APPROPRIATE NUMPY LINALG FUNCTION

print(xvec)
