# Contest No.: ABC167
# Problem No.: C
# Solver:      JEMINI
# Date:        20200510

import sys

def main():
    n, m, x = map(int, sys.stdin.readline().split())
    table = []

    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, m + 1):
        temp = 0
        for j in range(n):
            temp += table[j][i]
        if temp < x:
            print(-1)
            return
    ans = 0
    for i in range(n):
        ans += table[i][0]
    for i in range(1, 2 ** n):
        temp = i
        cnt = 0
        tempList = [0] * (m + 1)
        while temp > 0:
            if temp % 2:
                for j in range(m + 1):
                    tempList[j] += table[cnt][j]
            temp >>= 1
            cnt += 1
        flag = True
        for j in range(1, m + 1):
            if tempList[j] < x:
                flag = False
                break
        if flag:
            ans = min(ans, tempList[0])
    print(ans)    
    return

if __name__ == "__main__":
    main()