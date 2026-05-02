student = {
    "name" : "akash chaudhary",
    "subject" : ["physics","chemistry","math"],
    "marks" : {
        "physics" :98.3,
        "chemistry" :89.3,
        "math" : 99
        }
}
print(student["marks"]["math"])

#methods
print(student.keys())

#typecasting
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items()) #frist pair #reurn tuples
print(list(student.items())) #typecast to list

pairs=list(student.items())
print(pairs[0]) #access pair

#to return value of key
print(student["name"])
# print(student["name2"]) #give error
print(student.get("name"))
print(student.get("name2")) #print null value

student.update({"city" : "butwal","age" : 26})
print(student)
