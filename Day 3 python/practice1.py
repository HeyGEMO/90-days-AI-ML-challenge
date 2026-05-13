dictionary ={
    "table" : ["a piece of furniture","list of facts & figures"], #we can use tuple as well
    "cat" : "a small animal"
}
print(dictionary)

subject = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print("Total classroom we need is :", len(subject))

marks = {}
x=int(input("enter physics:"))
marks.update({"physics": x})
x=int(input("enter chemistry:"))
marks.update({"chemistry": x})
x=int(input("enter math:"))
marks.update({"math":x})

print(marks)

