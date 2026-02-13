listObj=[10,20,30,40,50]
print(listObj)

del listObj[2] #removes element at index 2
print(listObj)

listObj.clear() #removes all elements from the list
print(listObj)

del listObj #deletes entire list object
print(listObj) #NameError: name 'listObj' is not defined