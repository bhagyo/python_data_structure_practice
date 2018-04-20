arr = []
st = []
a = int(input('how manny numbers: '))
for i in range(a):
    b = input()
    arr.append(b)
cnt = 0
for i in range(a):
    st = arr[i]
    if len(st) > 1 and st[0] == st[len(st) - 1]:
        cnt += 1
print(cnt)
