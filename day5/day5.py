from read_input import read_input
import re

stacks = []

def moveP2(line):
    processedLine = line
    # extract numbers out of line
    # move 1 from 5 to 9
    processedLine = processedLine.replace("move ", "")
    processedLine = processedLine.replace("from ", "")
    processedLine = processedLine.replace("to ", "")
    indices = processedLine.split(' ')
    indices = [int(x) for x in indices]
    # print(indices)
    # print(processedLine)
    # number, from, to

    # remove last x variables from *from* stack
    # append these onto *to* stack
    fromIndex = indices[1] - 1
    toIndex = indices[2] - 1
    held = stacks[fromIndex][-indices[0]:]
    print(held)
    stacks[toIndex] += held
    print(stacks[toIndex])
    del stacks[fromIndex][-indices[0]:]

    #held = stacks[indices[1] - 1].pop(range(len(stacks[indices[1]]) - indices[0], len(stacks[indices[1]])))

    #stacks[indices[2 - 1]].append(held)

def moveP1(line):
    processedLine = line
    #extract numbers out of line
    # move 1 from 5 to 9
    processedLine = processedLine.replace("move ", "")
    processedLine = processedLine.replace("from ", "")
    processedLine = processedLine.replace("to ", "")
    indices = processedLine.split(' ')
    indices = [int(x) for x in indices]
    #print(indices)
    #print(processedLine)
    # number, from, to
    for i in range(indices[0]):
        held = stacks[indices[1] - 1].pop()
        stacks[indices[2] - 1].append(held)


if __name__ == '__main__':
    lines = read_input('../day5/input.txt')
    moves = []
    crates = []

    numberIndex = -1
    for i in range(0, len(lines)):
        print(lines[i])
        if " 1 " in lines[i]:
            numberIndex = i
            break

    crates = lines[0:numberIndex]
    moves = lines[numberIndex + 2:]
    # 1, 5, 9, 13, 17, etc.
    cleanCrates = []
    for crate in crates:
        cleanCrate = ""
        for i in range(0,len(crate)):
            if (i-1) % 4 == 0:
                cleanCrate += crate[i]
        cleanCrates.append(cleanCrate)

    print(crates)
    print(cleanCrates)
    print(moves)

    stacks = []
    cleanCrates.reverse()

    #add first line
    for crate in cleanCrates[0]:
        stacks.append([crate])

    print(stacks)

    for x in range(1, len(cleanCrates)):
        for i in range(0,len(cleanCrates[x])):
            if(cleanCrates[x][i] != ' '):
                stacks[i].append(cleanCrates[x][i])

    print(stacks)

    for line in moves:
        moveP2(line)
        print(stacks)

    #get top of every stack (last element in every stack)
    result = ""
    for stack in stacks:
        result += stack[-1]

    print(result)


