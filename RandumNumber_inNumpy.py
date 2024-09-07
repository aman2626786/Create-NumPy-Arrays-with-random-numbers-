import numpy as np
# Randum Functions
#1.rand() :-The function used to generate a random value between o to 1.
#2. randn() :-The function is usen to generate a random value closed to zero. This may return positive or negative number as well.
#3.ranf() :-The function for doing random sampling in numpy. It returns an array of specified shape and fills it with random flots in the half open intervel [0.0,1.0).
#4.randint() :- The function is used to generate a random number for given number.
# For example:
var1 = np.random.rand(5)
var2 = np.random.rand(5,6)
print(var1) 
print() 
print(var2)
print()
var2 = np.random.randn(10)
print(var2)
print()
var3 = np.random.ranf(6)
print(var3)
print()
var4 = np.random.randint(2,12,5)
print(var4)
print()