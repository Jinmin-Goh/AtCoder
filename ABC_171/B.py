# Contest No.: ABC171
# Problem No.: B
# Solver:      JEMINI
# Date:        20200621

import sys
import heapq

def main():
    n, k = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    print(sum(nums[:k]))
    return

if __name__ == "__main__":
    main()