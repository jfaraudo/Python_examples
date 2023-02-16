#
# INTRODUCTION TO PYTHON 
# Numerical calculation of a derivative
# Jordi Faraudo
# 

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

#Define a function
def my_function(u):
    w = 2.0*np.pi
    f= np.sin(w*u)
    return f

# Here we create a list of values for variable x from 0.0 to 2.0 each 0.1
x_list = np.arange(0.0, 2.0, 0.01)

# Calculate a set of values by appplying the function to x
y = my_function(x_list)

# create an empty list for the derivative
x_derivative = []
dy = []
    
#Calculate numerical derivative and add the result to the list dy
i=0
imax=len(x_list)-1
while i<imax:

     diffx=x_list[i+1]-x_list[i]
     diffy=y[i+1]-y[i]
     dy.append(diffy/diffx)
     x_derivative.append(x_list[i])
     i=i+1

# Create a plot the sets y and z as a function of x
plt.plot(x_list, y, 'r', x_derivative, dy, 'b')

#Add labels
plt.xlabel('x')
plt.ylabel('f and df/dx')
plt.title('Numerical calculation of derivative')
plt.legend(['f(x)', 'df/dx'])

#Show the plot in screen
plt.show()


