dic = {}
sz = int(input('size of dictionaris\n'))
for i in range(sz):
    x = str(input())
    y = input()
    dic.update({x: y})
for x, y in dic.items():
    print(x, y)
