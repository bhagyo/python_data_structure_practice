arr = []
a = int(input('how manny numbers: '))
##i = 0
for i in range(a):
    b = int(input('Enter number: '))
    arr.append(b)
mx = -9999999999
for i in range(a):
    mx = max(mx, arr[i])
print(mx)
