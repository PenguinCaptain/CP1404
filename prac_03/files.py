# 1.
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
content = in_file.read().strip()
print(f"Hi {content}!")
in_file.close()

# 3.
with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
print(num1 + num2)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        num = int(line)
        total += num
print(total)
