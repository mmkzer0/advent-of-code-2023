import sys
import re

input = sys.stdin

def findDigitSum(x):
    sum = int()

    for line in x:
        line = re.findall(r'\d+', line)
        line = ''.join(line)
        
        if len(line) == 1:
            sum += int(line[0]*2)
        else:
            sum += int(line[0] + line[-1])

    return sum

print(findDigitSum(input))