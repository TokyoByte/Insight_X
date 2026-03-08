for i in range(1, 10, 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

a = [2, 7, 1, 34, 3]
a.sort()

print(a)

del a[0]

print(a)
a = [10, 20, 30, 40, 50]


b = ("Henry", "Romeo", "Alan", "Mark")
print(b[0], b[-1])