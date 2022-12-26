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
count = 0
for _ in data:
    count += 1
    if _ == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break

print(count)
