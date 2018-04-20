dic = {}
sz = int(input('size of dictionaris\n'))
for i in range(sz):
    x = str(input())
    y = int(input())
    dic.update({x: y})


tot = int()
tot = 0
for x, y in dic.items():
    tot += y
print(tot)
