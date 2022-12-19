import math

from read_input import read_input
from math import ceil

class Monkey:
    def __init__(self, _number):
        self.number = _number
        self.items = []
        self.add_operation = False
        self.left_operand = ""
        self.right_operand = ""
        self.divisibleTest = -1
        self.true_monkey = -1
        self.false_monkey = -1
        self.inspects = 0

    def test(self):

        return False


def simulate_turn(monkeys, lcm):
    for i in range(len(monkeys.values())):
        print(f"monkey {i}")
        monkey = monkeys[i]
        for item in monkey.items:
            #print(f"Monkey {monkey.number} inspecting item with worry level of {item}")
            monkey.inspects += 1
            #run operation
            operation_result = 0
            temp_left = 0
            temp_right = 0
            if monkey.left_operand == "old":
                temp_left = item
            else:
                temp_left = monkey.left_operand

            if monkey.right_operand == "old":
                temp_right = item
            else:
                temp_right = monkey.right_operand

            if monkey.add_operation:
                operation_result = temp_left + temp_right
            else:
                operation_result = temp_left * temp_right

            operation_char = '+' if monkey.add_operation else '*'

            item = operation_result
            # print(f"worry level = {temp_left} {operation_char} {temp_right} = {item}")
            # divide by 3
            #item =  int(item / 3)
            item = item % lcm
            #print(f"Monkey no longer interested. Worry level now {item}")
            # test
            result = item % monkey.divisibleTest == 0
            # throw
            target_monkey = None
            if result == True:
                target_monkey = monkeys[monkey.true_monkey]

            else:
                target_monkey = monkeys[monkey.false_monkey]

            #print("operation " + "passed" if result else "failed")

            #print(f"Monkey {monkey.number} throwing item with value {item} "
            #      f"to monkey {target_monkey.number}")
            target_monkey.items.append(item)
        monkey.items = []

    return monkeys

if __name__ == '__main__':
    lines = read_input('../day11/input.txt')
    lines = [line.strip() for line in lines]
    monkeys = {}
    #print(lines)
    currentMonkey = None
    for line in lines:
        #new monkey
        if line.startswith("Monkey "):
            currentMonkey = Monkey(int(line[7]))
            monkeys[currentMonkey.number] = currentMonkey
            print(f"Made monkey {currentMonkey.number}")
            continue
        elif "Starting items: " in line:
            list = line.replace("Starting items: ", "")
            list = list.split(', ')
            list = [int(n) for n in list]
            print(list)
            currentMonkey.items = list
        elif "Operation: " in line:
            line = line.replace("Operation: new = ", "")
            line = line.split(' ')
            #print(line)
            if line[0] == "old":
                currentMonkey.left_operand = line[0]
            elif line[0].isnumeric():
                currentMonkey.left_operand = int(line[0])
            else:
                print(f"unknown left operand: {line[0]}")

            if line[2] == "old":
                currentMonkey.right_operand = line[2]
            elif line[2].isnumeric():
                currentMonkey.right_operand = int(line[2])
            else:
                print(f"unknown right operand: {line[2]}")

            if line[1] == '+':
                currentMonkey.add_operation = True
            elif line[1] == '*':
                currentMonkey.add_operation = False
            else:
                print(f"unknown operation: {line[1]}")
        elif "Test: " in line:
            line = line.replace("Test: divisible by ", "")
            currentMonkey.divisibleTest = int(line)
        elif "If true: throw to monkey " in line:
            line = line.replace("If true: throw to monkey ", "")
            currentMonkey.true_monkey = int(line)
        elif "If false: throw to monkey " in line:
            line = line.replace("If false: throw to monkey ", "")
            currentMonkey.false_monkey = int(line)

    print("done loading monkeys!")
    lcm = 0
    tests = [monkey.divisibleTest for monkey in monkeys.values()]
    lcm = tests[0]
    for i in range(1, len(tests)):
        lcm *= tests[i]

    print("simulating 10000 turns")

    for i in range(1,10001):
        print(f"simulating turn {i}")
        monkeys = simulate_turn(monkeys, lcm)

    #print results:
    print("After 10000 rounds: ")
    for monkey in monkeys.values():
        string_items = [str(item) for item in monkey.items]
        print(f"Monkey {monkey.number}: {', '.join(string_items)}. Inspected {monkey.inspects} items")

    inspect_list = [monkey.inspects for monkey in monkeys.values()]
    inspect_list.sort(reverse=True)
    print(inspect_list[0] * inspect_list[1])





