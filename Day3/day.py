x = 0
y = 0

with open("input.txt") as f:
    data = f.read()

houses = {
    (x, y): 1
}

for direction in data:
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    if (x, y) in houses:
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

count = len([k for k, v in houses.items() if v >= 1])
print(count)
