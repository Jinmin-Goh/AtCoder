# Contest No.: ABC167
# Problem No.: A
# Solver:      JEMINI
# Date:        20200510

import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    ans = 0
    if m == 1:
        if k != n - 1:
            print(0)
        else:
            print(1)
        return
    if n == 1:
        print(m)
        return
    
    allAns = 0

    for i in range(1, k + 1):
        ans = 1
        temp = n - 1 - i
        while temp > 0:
            cnt = 0
            tempAns = (m - 1) % 998244353
            while 2 ** (cnt + 1) <= temp:
                cnt += 1
                tempAns *= tempAns
                tempAns = tempAns % 998244353
            ans *= tempAns
            ans = ans % 998244353
            temp -= 2 ** cnt
        ans *= m
        ans = ans % 998244353

        temp = i - 1
        while temp > 0:
            cnt = 0
            tempAns = 2
            while 2 ** (cnt + 1) <= temp:
                cnt += 1
                tempAns *= tempAns
                tempAns = tempAns % 998244353
            ans *= tempAns
            ans = ans % 998244353
            temp -= 2 ** cnt
        allAns += ans
    
    temp = n - 1
    while temp > 0:
        cnt = 0
        tempAns = (m - 1) % 998244353
        while 2 ** (cnt + 1) <= m:
            cnt += 1
            tempAns *= tempAns
            tempAns = tempAns % 998244353
        ans *= tempAns
        ans = ans % 998244353
        temp -= cnt
    ans *= m
    ans = ans % 998244353
    
    print(ans)
    return

if __name__ == "__main__":
    main()