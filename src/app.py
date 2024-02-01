sum = 0

file = open('day1_input.txt')

lines = file.readlines()

for i in range(lines.__len__()):
    line = lines[i]
    digitsLine = []
    for j in range(line.__len__()):
        if(line[j].isdigit()):
            digitsLine.append(line[j])
    if(digitsLine.__len__() == 1):
        # print((str(digitsLine[0]) + str(digitsLine[0])))
        sum += int(str(digitsLine[0]) + str(digitsLine[0]))
    else:
        lastIndex = digitsLine.__len__() - 1
        # print(str(digitsLine[0]) + str(digitsLine[lastIndex]))
        sum += int(str(digitsLine[0]) + str(digitsLine[lastIndex]))
    # print(f'{line} && {digitsLine}')

print(sum)
