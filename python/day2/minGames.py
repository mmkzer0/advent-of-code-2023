import sys
import re

games = sys.stdin

def findGames(x):
    gID = int()
    for line in x:
        r = int((max([int(char) for char in re.findall(r"(\d+) red", line)])))
        g = int((max([int(char) for char in re.findall(r"(\d+) green", line)])))
        b = int((max([int(char) for char in re.findall(r"(\d+) blue", line)])))
        gID += (r*g*b)
    return gID

print(findGames(games))
