with open("D:\90 days AI Ml\Day 5\Demo.txt","r") as f:
    data=f.read()
    print(data)
#automatic close file with with
with open("D:\90 days AI Ml\Day 5\Demo.txt","w") as f:
    f.write("new data")
    