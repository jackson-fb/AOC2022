import os, sys
from PIL import Image, ImageShow

from read_input import read_input

class Tree:
    def __init__(self, height):
        self.visible_west = True
        self.visible_east = True
        self.visible_north = True
        self.visible_south = True
        self.distance_west = 0
        self.distance_east = 0
        self.distance_north = 0
        self.distance_south = 0
        self.height = height
        self.scenic_score = 0

def set_visible(grid, x,y):
    height = len(grid)
    width = len(grid[0])
    target = grid[x][y]
    #validate north
    for test_y in range(y-1, -1, -1):
        target.distance_north += 1
        if(grid[x][test_y].height >= target.height):
            target.visible_north = False
            break

    #validate south
    for test_y in range(y + 1,height):
        target.distance_south += 1
        if(grid[x][test_y].height >= target.height):
            target.visible_south = False
            break

    #validate west
    for test_x in range(x-1, -1, -1):
        target.distance_west += 1
        print(f"west: this tree at {x} current index {test_x}")
        if(grid[test_x][y].height >= target.height):
            target.visible_west = False
            break

    #validate east
    for test_x in range(x + 1,width):
        target.distance_east += 1
        if(grid[test_x][y].height >= target.height):
            target.visible_east = False
            break

    target.scenic_score = target.distance_west * target.distance_east * \
                          target.distance_north * target.distance_south


if __name__ == '__main__':
    lines = read_input('../day8/input.txt')
    print(lines)
    grid = []
    #init grid with rows
    for y in range(len(lines)):
        grid.append([])
        for x in range(len(lines[y])):
            grid[-1].append(Tree(int(lines[y][x])))

    preview = Image.new("RGBA", [len(lines[0]), len(lines)])
    print(grid)

    step = int(255 / 10)
    totalVisible = 0
    highestScore = 0
    bestTree = None
    highestCoords = (0,0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            set_visible(grid, x,y)
            #g = 255 if grid[x][y].visible_north == True else 0
            #b = 255 if grid[x][y].visible_south == True else 0
            #preview.putpixel([x,y], (step * grid[y][x].height,g,b))
            target = grid[x][y]
            height = target.height
            visible = target.visible_north or target.visible_south \
                      or target.visible_east or target.visible_west
            if visible:
                totalVisible += 1
            #preview.putpixel([y,x], ((step * height) if visible else 0,0,0,255))
            preview.putpixel([y,x], (255,255,255) if visible else (0,0,0))

            if target.scenic_score > highestScore:
                highestScore = target.scenic_score
                highestCoords = (x,y)
                bestTree = target


    ImageShow.show(preview)
    print(totalVisible)
    print(f"Highest score: {highestScore} at {highestCoords}")
