"""
This Python3 script loads a data file and tests two types
of fits using the fit_data module that was developed in EP 271.
"""

import numpy as np
from fit_data import *

# Open the desired data file.

# SUBSTITUTE THE NAME OF THE ASSIGNED FILE WITHIN THE QUOTES.

filename= 'exam2dataset1.dat'
datafile=open(filename,'r')

# Read the data file assuming two data values per line.

datalist=[]
for line in datafile:
    datalist.append([float(line.split()[0]), float(line.split()[1])])

# Convert the data to a NumPy array.

dataarray=np.array(datalist)

# PERFORM THE FIRST FIT ON DATAARRAY AND PRINT THE RESULTING COEFFICIENTS.

print(poly_fit(dataarray,2))

print(exp_fit(dataarray))


# PERFORM THE SECOND FIT ON DATAARRAY AND PRINT THE RESULTING COEFFICIENTS.
