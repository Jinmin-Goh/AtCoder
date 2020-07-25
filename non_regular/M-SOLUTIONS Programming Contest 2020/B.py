# Contest No.: M-SOLUTIONS Programming Contest 2020
# Problem No.: B
# Solver:      JEMINI
# Date:        20200725

import sys
import heapq

def main():
    a, b, c = map(int, input().split())
    k = int(input())
    cnt = 0
    while cnt <= k and a >= b:
        b *= 2
        cnt += 1
    if cnt > k:
        print("No")
        return
    while cnt <= k and b >= c:
        c *= 2
        cnt += 1
    if cnt > k:
        print("No")
    else:
        print("Yes")

    return

if __name__ == "__main__":
    main()