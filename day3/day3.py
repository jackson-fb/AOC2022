from read_input import read_input

def get_priority(item):
    item_ord = ord(item)
    lowerA = ord('a')
    lowerZ = ord('z')
    upperA = ord('A')
    upperZ = ord('Z')

    if(lowerA <= item_ord <= lowerZ):
        # lower
        return item_ord - lowerA + 1
    elif (upperA <= item_ord <= upperZ):
        return item_ord - upperA + 26 + 1


if __name__ == '__main__':
    lines = read_input('../day3/input.txt')

    # print("tests:")
    # print("{} should = 1".format(get_priority('a')))
    # print("{} should = 26".format(get_priority('z')))
    # print("{} should = 27".format(get_priority('A')))
    # print("{} should = 52".format(get_priority('Z')))

    # part 1:
    total_priority = 0
    for line in lines:
        half = int(len(line)/2)
        h1 = line[0:half]
        h2 = line[half:]

        for item in h1:
            if item in h2:
                total_priority += get_priority(item)
                break

    print(total_priority)

    # part 2:
    # combine every three lines, find item that appears exactly 3 times
    total_priority = 0
    for i in range(0, len(lines), 3):
        print(lines[i])
        print(lines[i+1])
        print(lines[i+2])

        for char in lines[i]:
            if char in lines[i+1] and char in lines[i+2]:
                print(char)
                total_priority += get_priority(char)
                break

    print(total_priority)
