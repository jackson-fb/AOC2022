from read_input import read_input
from PIL import Image, ImageShow

if __name__ == '__main__':
    #74,246,38
    render = Image.new("RGB", (40, 6))
    lines = read_input('../day10/input.txt')
    print(lines)
    splitlines = [line.split(' ') for line in lines]
    for line in splitlines:
        if(line[0] == "addx"):
            line[1] = int(line[1])

    reg = 1
    cycle = 0
    history = [0]
    for line in splitlines:
        if(line[0] == "noop"):
            cycle += 1
            history.append(reg)
        elif line[0] == "addx":
            history.append(reg)
            reg += line[1]
            history.append(reg)

    target_cycles = [20, 60, 100, 140, 180, 220]
    sum = 0
    for cycle in target_cycles:
        sum += history[cycle-1] * cycle

    print(f"p1 sum: {sum}")

    #draw image
    for x in range(0, len(history)):
        row = int(x / 40)
        col = x % 40
        spriteX = history[x]
        # DRAW
        lit = col in (spriteX - 1, spriteX, spriteX + 1)
        if lit:
            render.putpixel((col, row), (74, 246, 38))
        print(f"end of cycle {x}: reg: {history[x]}")
        # MOVE SPRITE
        spriteX = history[x]
        print(f"{col},{row}")
    render.show()
