tu = ()
x = int(input())
for i in range(x):
    v = int(input())
    tu += (v,)
v = int(input('which data to be found\n'))
v = tu.count(v)
if v == 0:
    print("the data is not here")
else:
    print("the data is here")
