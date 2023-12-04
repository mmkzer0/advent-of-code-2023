import sys
import re

input = sys.stdin
replacements = {"one" : "o1e", "two" : "t2o", "three" : "thr3e", "four" : "fo4r", "five" : "fi5e", "six" : "s6x", "seven" : "se7en", "eight" : "ei8ht", "nine" : "ni9e"}

def findDigitSum(x):
    sum = int()

    for line in x:
        for old, new in replacements.items():
            line = line.replace(old, new)

        line = re.findall(r'\d+', line)
        line = ''.join(line)

        if len(line) == 1:
            sum += int(line[0]*2)
        else:
            sum += int(line[0] + line[-1])

    return sum

print(findDigitSum(input))