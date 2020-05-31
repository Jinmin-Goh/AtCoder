# Contest No.: ABC169
# Problem No.: B
# Solver:      JEMINI
# Date:        20200531

import sys
import heapq

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    ans = 1
    for i in nums:
        if i == 0:
            ans = 0
            break
        if ans > 10 ** 18:
            continue
        ans *= i
    if ans > 10 ** 18:
        print(-1)
    else:
        print(ans)
    return

if __name__ == "__main__":
    main()