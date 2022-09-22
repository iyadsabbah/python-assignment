lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input('Enter a number: '))

    lst.append(ele)
print(f'The max number is : {max(lst)}')
