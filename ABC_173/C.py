# Contest No.: ABC173
# Problem No.: C
# Solver:      JEMINI
# Date:        20200705

import sys
import heapq

def main():
    h, w, K = map(int, input().split())
    table = []
    for _ in range(h):
        temp = input()
        table.append([])
        for i in temp:
            table[-1].append(i)    
    ans = 0
    for i in range(2 ** (w + h)):
        cnt = 0
        tempTable = [_[:] for _ in table]

        rowNum = i % (2 ** h)
        colNum = i // (2 ** h)
        cntRow = 0
        cntCol = 0

        while rowNum:
            if rowNum % 2:
                tempTable[cntRow] = ["R"] * w
            rowNum = rowNum // 2
            cntRow += 1
        while colNum:
            if colNum % 2:
                for j in range(h):
                    tempTable[j][cntCol] = "R"
            colNum = colNum // 2
            cntCol += 1
        for j in range(h):
            for k in range(w):
                if tempTable[j][k] == "#":
                    cnt += 1
        #print(i, cnt, K, tempTable)
        if cnt == K:
            ans += 1

    print(ans)


    return

if __name__ == "__main__":
    main()