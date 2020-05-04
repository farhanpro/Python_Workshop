import numpy as np 
x = np.arange(25).reshape(5,5)
print(x)
print(x[3,2])#Will print the element which is in 3rd row and 2nd position starting from 0
print(x[2:5,1:4])#Slicing will print elements which are in 2ndrow till 5throw and 2ndcolum and 5colum
print(x[0:3,0:3])#will print elements which are in 0row till 2ndrow and 0colum and 2ndcolum
y = np.arange(20)
print(y[y > 14])#This Will print the numbers which are greater than 14 in y array