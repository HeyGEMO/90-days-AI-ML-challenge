#methods
#set mutable
#elements in set is immutable

collection =set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("lassan insaan")
#cant pass list or dictionary unhashable
print(collection)
collection.remove(3)
print(collection)

collection.pop() #random pop
print(collection)

collection.clear()
print(collection)

