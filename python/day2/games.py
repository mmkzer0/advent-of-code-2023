import sys
import re

# [red, green, blue]
bounds = [12, 13, 14]
games = sys.stdin

def findGames(x, y):
    cubes = []
    gID = int()
    for line in x:
        game = int(re.search(r"Game (\d+)", line).group(1))
        cubes.append(max([int(char) for char in re.findall(r"(\d+) red", line)]))
        cubes.append(max([int(char) for char in re.findall(r"(\d+) green", line)]))
        cubes.append(max([int(char) for char in re.findall(r"(\d+) blue", line)]))
        if all(m >= n for m, n in zip(y, cubes)):
            gID += game
        cubes = []
    return gID

print(findGames(games, bounds))
