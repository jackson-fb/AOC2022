from read_input import read_input


if __name__ == '__main__':
    lines = read_input('input.txt')
    elves = [0]
    for line in lines:
        if line == '':
            elves.append(0)
            continue
        elves[len(elves)-1] += int(line)

    elves.sort(reverse=True)
    print(elves)
    print("part 1: {}\npart 2: {}".format(elves[0], sum(elves[0:3])))
