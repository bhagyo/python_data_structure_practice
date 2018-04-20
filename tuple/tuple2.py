tup = ()
x = int(input('size of tuple\n'))
for i in range(x):
    print('which type of data\n')
    print("1 for integer")
    print("2 for string")
    print("3 for boolean")
    typ = int(input())
    if typ == 1:
        vl = int(input())
    if typ == 2:
        vl = input()
    if typ == 3:
        vl = bool(input())
    tup += (vl,)
print(tup)
