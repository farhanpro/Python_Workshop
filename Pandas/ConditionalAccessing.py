import numpy as np 
import pandas as pd 
A = [1,2,3,4]
B = [5,6,7,8]
C = [9,10,11,12]
D = [13,14,15,16]
df = pd.DataFrame([A,B,C,D],['A','B','C','D'],['A1','B1','C1','D1'])#A,B,C,D will be denoted as rows and A1,A2,A3,A4 will be denoted as coloumn  
df['E1'] = df['D1'] + df['C1'] #adding a new column in our list
#df['E'] = df['D'] + df['C']
df.drop('D' , inplace = True) #This Will permanently delete the row 
df.drop('E1',axis = 1 , inplace =  True) #This method is used to delete a coloumn permamently 
print(df['D1']) #To access a single column
print(df.loc['A'])#To access a single Row (loc stands for location)
print(df.loc['C','D1'])#To access a single element
print(df>3)#To get values which are gerater than 3 in boolean form
print(df[df > 3])#To get values which are gerater than 3.
