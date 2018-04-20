tu = ()
x = int(input())
for i in range(x):
    v = int(input())
    tu += (v,)
v = int(input('which data to be found\n'))
print(tu.count(v))
