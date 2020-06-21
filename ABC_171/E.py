# Contest No.: ABC171
# Problem No.: E
# Solver:      JEMINI
# Date:        20200621

import sys
import heapq

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))

    refVal = nums[0]
    for i in range(1, n):
        refVal ^= nums[i]
    for i in nums:
        print(refVal ^ i, end = " ")
    return

if __name__ == "__main__":
    main()