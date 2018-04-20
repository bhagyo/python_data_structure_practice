arr = []
a = int(input('how manny numbers: '))
#i = 0
for i in range(a):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key=lambda x: x[0])
for i in range(a):
    print(arr[i])
# print(arr)
