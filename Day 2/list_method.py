list=[5,4,3,1,2]
fruit=['mango','guava','grapes','banana']
list.append(6)
#print(list.append(6)) return none
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
fruit.reverse()
print(fruit)
fruit.insert(4,'orange')
print(fruit)
list.remove(6) #remove value
print(list)
fruit.pop(1) #remove data from index
print(fruit)