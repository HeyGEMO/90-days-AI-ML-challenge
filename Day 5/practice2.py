#with open("D:\90 days AI Ml\Day 5\practice2.txt","w") as f:
#    f.write("1,2,3,4,5,6,7,9,54,23,12")
count =0
with open("D:\90 days AI Ml\Day 5\practice2.txt","r") as f:
    data=f.read()

    num=data.split(",")
    for val in num:
        if(int(val)%2==0):
            count += 1
print(count)
