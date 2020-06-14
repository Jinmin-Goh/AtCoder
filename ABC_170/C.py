# Contest No.: ABC170
# Problem No.: C
# Solver:      JEMINI
# Date:        20200614

import sys
import heapq

def main():
    x, n = map(int, input().split()) 
    nums = list(map(int, sys.stdin.readline().split()))
    if x not in nums:
        print(x)
        return
    
    #nums.sort()
    ans = None
    diff = 1
    while True:
        if x - diff not in nums:
            ans = x - diff
            break
        elif x + diff not in nums:
            ans = x + diff
            break
        diff += 1

    print(ans)
        
        
    
    return

if __name__ == "__main__":
    main()