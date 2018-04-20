
import operator
dic = {}
sz = int(input('size of dictionaris\n'))
for i in range(sz):
    x = str(input())
    y = input()
    dic.update({x: y})
print(dic)
ss = sorted(dic.items(), key=operator.itemgetter(0))
print(ss)
#print(OrderedDict(sorted(dic.items(), key=itemgetter(1), reverse=True)))
