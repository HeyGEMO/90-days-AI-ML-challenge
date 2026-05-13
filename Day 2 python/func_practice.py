list=[1,2,3,4,5,6,7]
hero=["parman","mangoman","padman"]
def length_list(list):
    print(len(list))
length_list(hero)

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(hero)