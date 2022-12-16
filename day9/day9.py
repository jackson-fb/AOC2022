from PIL import Image, ImageShow
from read_input import read_input

directions = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

def draw_gif(split_lines):

    # IMAGE DRAWING CODE
    preview = Image.new("HSV", (maxX + xShift + 1, maxY + yShift + 1))
    cursorPos = [0, 0]
    h = 0
    linesDone = 0
    for line in splitLines:
        distance = int(line[1])
        direction = directions[line[0]]
        h += 1
        if h > 255: h = 0
        for i in range(distance):
            cursorPos[0] += direction[0]
            cursorPos[1] += direction[1]

            # print(f"{cursorPos[0] + xShift}, {cursorPos[1] + yShift}")

            preview.putpixel((cursorPos[0] + xShift, cursorPos[1] + yShift), (h, 255, 255))
        linesDone += 1
        if (linesDone > movesperframe):
            linesDone = 0
            frames.append(preview.copy())

        # END OF IMAGE DRAWING CODE

    rgbframes = [frame.convert("RGBA") for frame in frames]

    # for i in range(len(rgbframes)):
    #    rgbframes[i].save(f"../testdir/{i}.png")
    rgbframes[0].save('../pillow_imagedraw.gif',
                      save_all=True, append_images=rgbframes[1:], optimize=False, duration=40, loop=0)
    ImageShow.show(preview)

def print_grid(grid):
    gridLines = []
    for y in range(len(grid[0])):
        lineString = ""
        for x in range(len(grid)):
            character = "."
            if grid[x][y] != '':
                character = grid[x][y]
            lineString += character + " "
        gridLines.append(lineString)

    gridLines.reverse()
    for gridLine in gridLines:
        print(gridLine)
    print()


def get_new_tail_position(head_pos, old_tail_pos):
    new_tail_pos = [old_tail_pos[0],old_tail_pos[1]]
    delta = [head_pos[0] - old_tail_pos[0],
             head_pos[1] - old_tail_pos[1]]

    if(abs(delta[0]) > 1 and delta[1] == 0):
        new_tail_pos[0] += int(delta[0] / abs(delta[0]))

    if (abs(delta[1]) > 1 and delta[0] == 0):
        new_tail_pos[1] += int(delta[1] / abs(delta[1]))

    if abs(delta[0]) + abs(delta[1]) >= 3:
        new_tail_pos[0] += int(delta[0] / abs(delta[0]))
        new_tail_pos[1] += int(delta[1] / abs(delta[1]))


    # if(delta[0] == 0 and delta[1] != 0):
    #     new_tail_pos = [old_tail_pos[0], old_tail_pos[1] + abs(delta[1])]
    #
    # if (delta[1] == 0 and delta[0] != 0):
    #     new_tail_pos = [old_tail_pos[0] + abs(delta[0]), old_tail_pos[1]]
    print(delta)
    return new_tail_pos

if __name__ == '__main__':
    frames = []
    movesperframe = 1
    lines = read_input('../day9/input.txt')
    #print(lines)
    splitLines = [line.split(' ') for line in lines]

    cursorPos = [0, 0]
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    numSteps = 0

    #find max x and y
    for line in splitLines:
        distance = int(line[1])
        direction = directions[line[0]]
        for i in range(distance):
            cursorPos[0] += direction[0]
            cursorPos[1] += direction[1]
            # print(cursorPos)
            numSteps += 1
            if cursorPos[0] < minX:
                minX = cursorPos[0]
            if cursorPos[0] > maxX:
                maxX = cursorPos[0]
            if cursorPos[1] < minY:
                minY = cursorPos[1]
            if cursorPos[1] > maxY:
                maxY = cursorPos[1]

    print(f"x: {minX}:{maxX}, y: {minY}:{maxY}")
    xShift = 0 - minX
    yShift = 0 - minY
    print(f"shifting {xShift}, {yShift}")
    print(f"x: {minX + xShift}:{maxX + xShift + 1}, y: {minY + yShift}:{maxY + yShift + 1}")
    print(f"num steps: {numSteps}")

    # init grid
    grid = []
    for x in range(maxX + xShift + 1):
        grid.append([])
        for y in range(maxY + yShift + 1):
            grid[-1].append('')

    headPos = [xShift,yShift]
    tailPos = [xShift,yShift]
    knots = [headPos, tailPos]
    knots *= 5
    #mark grid
    grid[headPos[0]][headPos[1]] = 'S'
    for line in splitLines:
        distance = int(line[1])
        direction = directions[line[0]]
        for i in range(distance):
            knots[0][0] += direction[0]
            knots[0][1] += direction[1]
            for k in range(1, len(knots)):
                knots[k] = get_new_tail_position(knots[k-1], knots[k])
            #tailPos = get_new_tail_position(headPos, tailPos)
            tailPos = knots[-1]
            grid[tailPos[0]][tailPos[1]] = '#'
            #print_grid(grid)

    visited = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if(grid[x][y]) == '#':
                visited += 1

    print("Done!")
    print(f"visited : {visited}")
