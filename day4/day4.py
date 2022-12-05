from read_input import read_input

def Overlaps(_r1, _r2):
    if r1[0] <= r2[0] <= r1[1] or r2[0] <= r1[0] <= r2[1]:
        print("overlap")
        return True

    print("no_overlap")
    return False

def Is_Encapsulated(_r1, _r2):


    # 2 inside 1
    if r1[0] <= r2[0] and r1[1] >= r2[1]:
        print("2 in 1")
        return True
    # 1 inside 2
    elif r2[0] <= r1[0] and r2[1] >= r1[1]:
        print("1 in 2")
        return True

    print("No")
    return False



if __name__ == '__main__':

    lines = read_input('../day4/input.txt')
    encapsulated_total = 0
    overlap_total = 0
    for line in lines:
        r1, r2 = line.split(',')
        r1 = r1.split('-')
        r2 = r2.split('-')

        r1 = [int(x) for x in r1]
        r2 = [int(x) for x in r2]
        print(r1, r2)
        print(line)
        result_encapsulated = Is_Encapsulated(r1, r2)
        result_overlap = Overlaps(r1, r2)
        if(result_encapsulated):
            encapsulated_total += 1
        if(result_overlap):
            overlap_total += 1

    print(encapsulated_total)
    print(overlap_total)
