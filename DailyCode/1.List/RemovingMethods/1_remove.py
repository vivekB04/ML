listObj=[10,20,30,40,50]
print(listObj)

listObj.remove(30)
print(listObj)

listObj.remove(100) #ValueError: list.remove(x): x not in list
print(listObj)