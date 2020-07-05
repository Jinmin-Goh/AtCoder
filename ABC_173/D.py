# Contest No.: ABC173
# Problem No.: D
# Solver:      JEMINI
# Date:        20200705

import sys
import heapq

def main():
    n = int(input())    
    nums = list(map(int, sys.stdin.readline().split()))

    nums.sort()
    ans = 0

    # initial
    temp = nums.pop()
    ans += temp
    n -= 2

    for i in range(n // 2):
        ans += nums[-i - 1] * 2

    if n % 2:
        ans += nums[-(n // 2) - 1]
    
    
    print(ans)

    return

if __name__ == "__main__":
    main()