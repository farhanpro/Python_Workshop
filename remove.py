list = [1,2,3,4]
print ("First phase",(list))
list.remove(3)
print("Second phase Remove",(list)) #remove()  is used to delete the value from the list
list.pop(0)
print("Third phase PoP",(list)) #PoP() is used to  delete  the index value from the list
list.append(5)
print("Fourth phase append",(list)) #Append() is used to  add a single object to list
list.extend([1,6])
print("Fifth phase extend",(list)) #Extend() 
list.remove(1)
list.insert(0,1)
print("Sixth phase",(list))#insert() takes an index value and an object as its argument
list.insert(1,"One and a half")
print("Seventh phase",(list))#insert() takes an index value and an object as its argument

