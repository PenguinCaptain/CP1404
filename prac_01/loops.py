for i in range(1, 21, 2):
    print(i, end=" ")
print()


# a.
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c.
n = int(input("Number of stars: "))
for _ in range(n):
    print("*", end="")
print()


# d. Print n lines of increasing stars
print("Print n lines of increasing stars:")
for i in range(1, n + 1):
    print("*" * i)
