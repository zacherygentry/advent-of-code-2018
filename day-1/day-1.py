import time


def part1():
    f = open("input.txt", "r")

    sum = 0

    for line in f:
        sum += int(line)

    print(sum)
    f.close()


def part2():
    counter = 0
    tic = time.clock()
    sum = 0
    arr = [0]
    while True:
        f = open("input.txt", "r")
        for line in f:
            num = int(line)
            sum += num
            if sum in arr:
                print(sum)
                toc = time.clock()
                print(toc - tic)
                return
            else:
                arr.append(sum)
        counter += 1
        print("Iterated " + str(counter) + " times")
        f.close()


part1()
part2()
