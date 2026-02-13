#Deepcopy
import copy
listObj1=[[10,20,30],[40,50,60]]
print(listObj1)

listObj2=copy.deepcopy(listObj1)
print(listObj2)

print(listObj1 is listObj2) #False
print(id(listObj1))
print(id(listObj2))

listObj1[0][2]=35
print(listObj1) 
print(listObj2)

listObj2[1][2]=65
print(listObj1) 
print(listObj2)

print(listObj1[0] is listObj2[0]) #False
print(listObj1[1][1] is listObj2[1][1]) #False

print(id(listObj1[1][1]))
print(id(listObj2[1][1]))