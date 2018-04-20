arr = []
a = int(input('how manny numbers: '))
##i = 0
for i in range(a):
    b = int(input('Enter number: '))
    arr.append(b)
mn = 9999999999
for i in range(a):
    mn = min(mn, arr[i])
print(mn)
