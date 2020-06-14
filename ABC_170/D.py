# Contest No.: ABC170
# Problem No.: D
# Solver:      JEMINI
# Date:        20200614

import sys
import heapq

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()

    check = [False] * (10 ** 6 + 1)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            check[nums[i]] = True
    #print(nums)
    ans = 0
    for i in range(n):
        if check[nums[i]] == False:
            ans += 1
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            cnt = nums[i] * 2
            while cnt < 10 ** 6 + 1:
                #print(cnt)
                check[cnt] = True
                cnt += nums[i]
        #print(ans)
    print(ans)

    
    return

if __name__ == "__main__":
    main()