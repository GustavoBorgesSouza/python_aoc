import re



def estrelinha(fileName):
    sum = 0

    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i in range(lines.__len__()):
        line = lines[i]
        digitsLine = getDigits(line)
        sum += int(str(digitsLine[0]) + str(digitsLine[-1]))
        print(str(digitsLine[0]) + str(digitsLine[-1]))
        # print(f'{line} && {digitsLine}')
    print(str(len(lines)) + '    | AAAAAAAAAAAAAAAAAAAAAAAAAAA')
    return sum

def getDigits(string):
        pattern = re.compile('(\d|one|two|three|four|five|six|seven|eight|nine)')
        find = []

        for c in range(len(string)):
            result = pattern.match(string, c)
            if(result is not None):
                find.append(result.group())

        for i, name in enumerate(find):
            if(name == 'one'):
                find[i] = 1
            if(name == 'two'):
                find[i] = 2
            if(name == 'three'):
                find[i] = 3
            if(name == 'four'):
                find[i] = 4
            if(name == 'five'):
                find[i] = 5
            if(name == 'six'):
                find[i] = 6
            if(name == 'seven'):
                find[i] = 7
            if(name == 'eight'):
                find[i] = 8
            if(name == 'nine'):
                find[i] = 9

        print(string)
        print(find)

        return find

print(estrelinha("src/day1_input.txt"))