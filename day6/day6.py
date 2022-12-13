from read_input import read_input


def check_unique(chunk):
    for char in chunk:
        if chunk.count(char) != 1:
            return False
    return True


def find_start_marker(datastream, width):
    left_index = 0
    right_index = width
    for i in range(len(datastream) - width):
        left_index = i
        right_index = i + width
        print("{}, {}".format(left_index, right_index))
        if(check_unique(datastream[left_index : right_index])):
            print("Found!")
            return right_index
    return -1


if __name__ == '__main__':
    lines = read_input('../day6/input.txt')
    print("p1")
    print(find_start_marker(lines[0], 4))
    print("p2")
    print(find_start_marker(lines[0], 14))
