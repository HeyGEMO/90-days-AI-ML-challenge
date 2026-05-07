#types of files
#text files-txt,docx,log etc
#binary files-mp4,mov,jpeg etc
#r reading default
#t text default

f=open("D:\90 days AI Ml\Day 5\Demo.txt", "r")
#data = f.read(5)
line1=f.readline()
line2=f.readline()
#print(data)
print(line1)
print(line2)
#print(type(data))
f.close()