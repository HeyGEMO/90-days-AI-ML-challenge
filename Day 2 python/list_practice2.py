list=[1,2,1]
copy_list=list.copy()
list.reverse()
if copy_list==list:
    print("this is palindrome")
else:
    print('not palindrome')