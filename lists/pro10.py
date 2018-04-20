ar = []
x = int(input('size of list\n'))
sz = int(input('size of words\n'))
print('give the input words\n')
for i in range(x):
    b = input()
    ar.append(b)
for i in range(x):
    if len(ar[i]) >= sz:
        print(ar[i])
