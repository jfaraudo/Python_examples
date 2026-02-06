#!/usr/bin/env python
# coding: utf-8

# ## Example parabolic motion

# Example of use of numpy and Matplotlib to plot data for a problem with known analytical solution

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# **Define Functions**

def parabolic(u,theta,dt):
    g=9.8 #m/s2
    t_flight = 2*u*np.sin(theta)/g #time until reaches y=0
    t = np.arange(0,t_flight,dt) #generate a list of all times from zero to end interval dt
    x=u*np.cos(theta)*t #calculate all positions x(t)
    y=u*np.sin(theta)*t - (1.0/2.0)*g*t*t #calculate all positions y(t)
    return x,y


# **Main program**

# *Initial velocity (angle and modulus)*
#Ask the user for angle
print("Enter desired launch angle in degrees (recommended 45 degrees):")
theta=float(input())
#convert angle in degrees to rad
theta = np.radians(theta)
print(theta, "rad")

#list of velocities
u_list=[20.0,40.0,60.0] #m/s

# *Solve the motion for all velocities with a time resolution of dt*

dt=0.001 #seconds
for u in u_list:
    x,y=parabolic(u,theta,dt)
    plt.plot(x, y)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile motion')
plt.show()





