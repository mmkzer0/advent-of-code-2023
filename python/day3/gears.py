import sys

gearmap = [line.strip() for line in sys.stdin]

def getNumMap(arr, index):
    line = arr[index]
    numTmp, startIndex, stopIndex = str(), None, None
    numMap = []

    for index, char in enumerate(line):
        if char.isdigit():
            numTmp += char
            if startIndex == None:
                startIndex = index
        elif numTmp != str():
            stopIndex = index - 1
            numMap.append([int(numTmp), startIndex, stopIndex])
            numTmp, startIndex, stopIndex = str(), None, None
    
    if numTmp != str():
        numMap.append([int(numTmp), startIndex, len(line)-1])

    return numMap


def getPartNum(inp):
    partNum = int(0)
    tmp = int(0)

    for i in range(0, len(inp)):
        lineNumMap = getNumMap(inp, i)
        if lineNumMap == []:
            continue
        #print(lineNumMap)

        curLine = inp[i]
        if i != 0:
            prevLine = inp[i - 1]
        if i <= len(inp) - 2:
            nxtLine = inp[i + 1]

        for numTup in lineNumMap:
            staI = numTup[1] - 1
            if numTup[1] == 0: staI = 0
            stoI = numTup[2] + 2
            if stoI >= len(curLine): stoI = numTup[2]

            for j in range(staI, stoI):
                if curLine[j].isdigit() == False and curLine[j] != ".":
                    partNum += numTup[0]
                    break
                if i > 0 and prevLine[j].isdigit() == False and prevLine[j] != ".":
                    partNum += numTup[0]
                    break
                elif i <= len(inp) - 2 and nxtLine[j].isdigit() == False and nxtLine[j] != ".":
                    partNum += numTup[0]
                    break
    return partNum

print(getPartNum(gearmap))