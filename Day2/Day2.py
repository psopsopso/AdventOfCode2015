with open("input.txt") as f:
    data = f.read().splitlines()


# Part 1
totalFeets = 0

for gift in data:
    dimensions = gift.split("x")
    l, w, h = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
    lw = 2*l*w
    wh = 2*w*h
    hl = 2*h*l
    totalFeetGift = lw+wh+hl + min(l*w, w*h, h*l)
    totalFeets += totalFeetGift

print(totalFeets)

totalFeets = 0

# Part 2


def day2():
    total = 0
    for line in open('input.txt'):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = 2 * min(l+w, w+h, h+l)
        bow = l*w*h
        total += ribbon + bow
    return total


print(day2())
