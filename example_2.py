#
# INTRODUCTION TO PYTHON 
# Example program by Jordi Faraudo
# 

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

#Define a function (in the computational sense)
def my_function(u):
    f1 = np.exp(u)
    f2 = np.exp(-u)
    return f1,f2

# Here we create a list of values for variable x from 0.0 to 2.0 each 0.1
x = np.arange(0.0, 2.0, 0.1)

# Calculate two new sets of values by appplying a function to x
y,z = my_function(x)

# Create a plot the sets y and z as a function of x
plt.plot(x, y, 'ro', x, z, 'bv')

#Show the plot in screen
plt.show()




