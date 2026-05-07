#with open("D:\90 days AI Ml\Day 5\practice.txt","w") as f:
    #f.write("Hi everyone \nwe are learning File I/O\n")
    #f.write("using java.\nI like programming java.")
def check_for_word():
    word="xlearning"
    with open("D:\90 days AI Ml\Day 5\practice.txt","r") as f:
        data=f.read()
        if(data.find(word)==word):
            print("found")
        else:
            print("not found")
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("D:\90 days AI Ml\Day 5\practice.txt","r") as f:
        while data:
            data= f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
#read replace data
#new_data=data.replace("java","python")
#print(new_data)
#overwrite
#with open("D:\90 days AI Ml\Day 5\practice.txt","w") as f:
#    f.write(new_data)    
check_for_word()
check_for_line()
    