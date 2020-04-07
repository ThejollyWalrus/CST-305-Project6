# Mason Hamilton & Dylan Nasser
# CST-305-1:55
# Professor Ricardo Citro
# 4/5/20
# Project 6 Taylor Polynomials
# Colobrated with Ryan and Michael and logan for help

#import libaries below
import sympy as sy
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy.functions import sin, cos


#Setting the inital values
deriv = [-1, 1, 0, 2, -2]
nth = 7
d = 5

#for loop for the derivatives
for k in range (100):
    ans = 2 * deriv[d-2] * (k + 3)
    deriv.append(ans)
    d = d + 1

#if or else stament return the value of the next factor
def factor(i):
    if i == 1:
        return i
    else:
        return factor(i-1) * i

#our main taylor fucntion that we find our value
def taylor(n , t):
    yValue = 1
    for i in range(n):
        yValue = (deriv[i+1]/factor(i+1))*t**(i+1) + yValue
    return yValue

#plugging in the values to get our appromation value
def modelT(p, t):

    return[p[1], t * 2 * p[1]-(t**2)*p[0]]

p0 = [1, -1]

x = np.linspace(0, 3.5)
mainFunc = odeint(modelT, p0, x)
print('\nValue of y(3.5): ', mainFunc[-1][0])
t = 3.5
print('Taylor ~Value of y(3.5), n = 4: ', 1 - t -(1/3)*t**3-(1/12)*t**4)

#the multiple functions for different powers
func1 = 1-x-(1/3)*x**3-(1/12)*x**4
func2 = 1-x-(1/3)*x**3-(1/12)*x**4-(1/10)*x**5
func3 = 1-x-(1/3)*x**3-(1/12)*x**4-(1/10)*x**5-(1/45)*x**6
func4 = 1-x-(1/3)*x**3-(1/12)*x**4-(1/10)*x**5-(1/45)*x**6-(1/42)*x**7

#out plt functions that print our graph with 5 differrent lines
plt.plot(x, mainFunc[:, 0], 'k-', label='Actual Odeint')
plt.plot(x,func1,'b--',label=' ~Value (n=4)')
plt.plot(x, func2,'r--',label=' ~Value (n=5)')
plt.plot(x, func3,'g--',label=' ~Value (n=6)')
plt.plot(x, func4,'y--',label=' ~Value(n=7)')
#makin small adjustments to our graph
plt.title('Taylor Polynomials part 1')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.ylim([-500, 0])
plt.show()