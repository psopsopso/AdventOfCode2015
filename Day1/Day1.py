# read input file

with open("input.txt") as f:
    data = f.read()

# Part 1

floor = 0
for _ in data:
    if _ == "(":
        floor += 1
    else:
        floor -= 1

print(floor)

# Part 2

floor = 0
for count, value in enumerate(data, start=1):
    if value == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(count)
        break
