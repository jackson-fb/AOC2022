from read_input import read_input

#rock, paper, scissors
#ABC is what opponent plays, XYZ is response

strategy =  [2,0,1,0,1,2,1,2,0]
results =   [3,0,6,6,3,0,0,6,3]

opponent_offset = ord('A')
player_offset = ord('X')

def get_result(opponent, player):
    result = results[opponent + (3 * player)]
    print("{} / {} = {}".format(opponent, player, result))
    print("{} + {} = {}".format(result, player, result+player))
    return result + player + 1


if __name__ == '__main__':
    lines = read_input('../day2/input.txt')
    p1total = 0
    p2total = 0
    for line in lines:
        splitline = line.split(' ')
        print(line)

        opponent = ord(splitline[0]) - opponent_offset
        player = ord(splitline[1]) - player_offset
        print("{}: {}, {}: {}".format(splitline[0], ord(splitline[0]), splitline[1], ord(splitline[1]) ))
        print("line: {} {}".format(opponent, player))

        p1total += get_result(opponent, player)
        p2total += get_result(opponent, strategy[opponent + (3 * player)])

    print(p1total)
    print(p2total)
