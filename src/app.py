import re

class ISolve:
    def solve(self) -> int:
        '''
        Method used for solving day one of advent of code 2023
        '''


class Solve(ISolve):
    def __init__(self,  fileName: str) -> None:
        self.fileName = fileName

    def solve(self, includeSpelled: bool | None = True) -> int:
        self.includeSpelled = includeSpelled

        sum = 0

        with open(self.fileName, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i in range(lines.__len__()):
            line = lines[i]
            digitsLine = getDigits(line,includeSpelled=includeSpelled)
            sum += int(str(digitsLine[0]) + str(digitsLine[-1]))
        return sum

def getDigits(string: str, includeSpelled: bool = True) -> list[int]:
        find = []

        if(includeSpelled):
            pattern = re.compile('(\d|one|two|three|four|five|six|seven|eight|nine)')
        else:
            pattern = re.compile('(\d)')

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

        return find

solver = Solve(fileName="src/day1_input.txt")

print(solver.solve(includeSpelled=False))
print(solver.solve())
