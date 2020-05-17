# Contest No.: ABC168
# Problem No.: E
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    modVal = 1000000007
    n = int(input())
    ppList = []
    pnList = []
    npList = []
    nnList = []
    znList = []
    nzList = []
    pzList = []
    zpList = []
    zzList = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if a > 0 and b > 0:
            ppList.append((a, b))
        elif a > 0 and b < 0:
            pnList.append((a, b))
        elif a < 0 and b > 0:
            npList.append((a, b))
        elif a < 0 and b < 0:
            nnList.append((a, b))
        elif a == 0 and b < 0:
            znList.append((a, b))
        elif a < 0 and b == 0:
            nzList.append((a, b))
        elif a == 0 and b > 0:
            zpList.append((a, b))
        elif a > 0 and b == 0:
            pzList.append((a, b))
        else:
            zzList.append((a, b))
    ans = 1

    # zp, zn, pz, nz
    zAns = 2 ** (len(zpList) + len(znList)) % modVal + 2 ** (len(pzList) + len(nzList)) % modVal - 1
    zAns = zAns % modVal
    ans = zAns

    # pp, pn, np, nn
    ratioDict = {}
    for i in ppList:
        gcdVal = gcd(i[0], i[1])
        ratio = (i[0] // gcdVal, i[1] // gcdVal)
        if ratio not in ratioDict:
            ratioDict[ratio] = [1, 0]
        else:
            ratioDict[ratio][0] += 1
    for i in nnList:
        gcdVal = gcd(-i[0], -i[1])
        ratio = (-i[0] // gcdVal, -i[1] // gcdVal)
        if ratio not in ratioDict:
            ratioDict[ratio] = [1, 0]
        else:
            ratioDict[ratio][0] += 1

    for i in npList:
        gcdVal = gcd(abs(i[0]), abs(i[1]))
        ratio = (abs(i[1]) // gcdVal, abs(i[0]) // gcdVal)
        if ratio not in ratioDict:
            ratioDict[ratio] = [0, 1]
        else:
            ratioDict[ratio][1] += 1
    for i in pnList:
        gcdVal = gcd(abs(i[0]), abs(i[1]))
        ratio = (abs(i[1]) // gcdVal, abs(i[0]) // gcdVal)
        if ratio not in ratioDict:
            ratioDict[ratio] = [0, 1]
        else:
            ratioDict[ratio][1] += 1
    for i in ratioDict:
        temp = 2 ** ratioDict[i][0] % modVal
        temp += (2 ** ratioDict[i][1] - 1) % modVal
        ans *= temp
        ans = ans % modVal

    ans -= 1
    ans += len(zzList)
    ans = ans % modVal
    print(ans)
    return

if __name__ == "__main__":
    main()