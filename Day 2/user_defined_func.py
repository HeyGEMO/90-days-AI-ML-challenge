def cal_prod(num1=1,num2=1): #default parameter
    print(num1*num2)
    return num1*num2

cal_prod()
cal_prod(2,3)

def cal_sub(a,b=1): #starting from last
    print(a-b)
cal_sub(4)