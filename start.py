a = [1, 2, 3, 4]

b=a.copy()

for i in b:
    index = b.index(i)*2
    print(index)
    a.insert(index, i+i)

print(a)