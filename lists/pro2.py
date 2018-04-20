arr = []
a = int(input('how manny numbers: '))
##i = 0
for i in range(a):
    b = int(input('Enter number: '))
    arr.append(b)
sum = 1
for i in range(a):
    sum *= arr[i]
print(sum)
