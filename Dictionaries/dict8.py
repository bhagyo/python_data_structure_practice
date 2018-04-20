
dic1 = {}
dic2 = {}
dic3 = {}
sz = int(input('size of dictionaris 1\n'))
for i in range(sz):
    x = str(input())
    y = input()
    dic1.update({x: y})
sz = int(input('size of dictionaris 2\n'))
for i in range(sz):
    x = str(input())
    y = input()
    dic2.update({x: y})
dic3 = dict(dic1)
dic3.update(dic2)
print(dic3)
