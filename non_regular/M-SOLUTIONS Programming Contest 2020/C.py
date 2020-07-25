# Contest No.: M-SOLUTIONS Programming Contest 2020
# Problem No.: C
# Solver:      JEMINI
# Date:        20200725

import sys
import heapq

def main():
    n, k = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(n - k):
        if nums[i] < nums[k + i]:
            print("Yes")
        else:
            print("No")
    return

if __name__ == "__main__":
    main()