import numpy as np 
x = np.arange(0,20)
print(x)  #Will print 0 to 19
print(x[8]) #Will print the value which is on the 8 position (8)
print(x[1]) #Will print the value which is on the 1 position (1)
print(x[:10]) #Will print the numbers which are before 10
print(x[10:]) #Will print the numbers which are after 9
print(x[2:5]) #Will print the numbers from 2 to 4 (5 will not be printed)
print(x[-20:-1])#Will print the number from 0 to 18 
y = x.copy()#All the Element of x will be copied into y 
y[-20:-1] = 80 #All the Element will be changed to 80
print(y)