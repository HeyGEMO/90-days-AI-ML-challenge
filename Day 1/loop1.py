nums= [1,2,3,4,5]
for num in nums:
    print(num)

nums= [1,2,3,4,5]
for num in nums:
    if num==3:
        print('found!')
        break
    print(num)

nums= [1,2,3,4,5]
for num in nums:
    if num==3:
        print('found!')
        continue
    print(num)

nums= [1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num,letter)

