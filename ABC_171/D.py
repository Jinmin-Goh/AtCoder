# Contest No.: ABC171
# Problem No.: D
# Solver:      JEMINI
# Date:        20200621

import sys
import heapq

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    cntList = [0] * (10 ** 5 + 1)
    for i in range(n):
        cntList[nums[i]] += 1
    sumVal = sum(nums)
    q = int(input())
    for _ in range(q):
        b, c = map(int, sys.stdin.readline().split())
        sumVal -= cntList[b] * b
        sumVal += cntList[b] * c
        cntList[c] += cntList[b]
        cntList[b] = 0
        print(sumVal)

    return

if __name__ == "__main__":
    main()