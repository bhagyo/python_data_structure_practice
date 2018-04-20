
def is_pre(x):
    if x in dic:
        print('yes')
    else:
        print('No')


dic = {}
sz = int(input('size of dictionaris\n'))
for i in range(sz):
    x = str(input())
    y = input()
    dic.update({x: y})
print('serach for')
serch = input()
is_pre(serch)
