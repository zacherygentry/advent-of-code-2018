
def part1():
    f = open("input.txt", "r")
    twos = 0
    threes = 0
    for line in f:
        unique = set(line)
        unique.discard("\n")
        got2 = False
        got3 = False
        for c in unique:
            count = line.count(c)
            if count == 2 and not got2:
                twos += 1
                got2 = True
            elif count == 3 and not got3:
                threes += 1
                got3 = True
    f.close()
    print(twos * threes)


def part2():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            counter = 0
            for k in range(0, len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    counter += 1
                    if counter > 1:
                        break
            if counter == 1:
                print(lines[i], lines[j])

part1()
part2()
