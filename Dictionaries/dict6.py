import operator
dic = {}
sz = int(input('size of dictionaris\n'))
for i in range(1, sz + 1):
    x = str(i)
    y = i * i
    dic.update({x: y})
ss = sorted(dic.items(), key=operator.itemgetter(0))
for x, y in ss:
    print(x, y)
