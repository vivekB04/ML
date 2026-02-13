#Shallow copy
import copy
listObj1=[[10,20,30],[40,50,60]]
print(listObj1)

listObj2=copy.copy(listObj1)
print(listObj2)

print(listObj1 is listObj2) #False
print(id(listObj1))
print(id(listObj2))

listObj1[0][2]=35
print(listObj1) 
print(listObj2)

print(listObj1[0] is listObj2[0]) #True
print(listObj1[1][1] is listObj2[1][1]) #True

print(id(listObj1[1][1]))
print(id(listObj2[1][1]))

