# Contest No.: ABC173
# Problem No.: E
# Solver:      JEMINI
# Date:        20200705

import sys
import heapq

def main():
    modVal = 10 ** 9 + 7
    # parsing
    n, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    
    # edge case; n == k
    if n == k:
        ans = 1
        for i in nums:
            ans *= i % modVal
            ans %= modVal
        print(ans % modVal)
        return
    
    # edge case; all neg
    if max(nums) < 0:
        nums.sort()
        ans = 1
        # odd k
        if k % 2:
            for i in range(k):
                ans *= nums[-i - 1] % modVal
                ans %= modVal
        # even k
        else:
            for i in range(k):
                ans *= nums[i] % modVal
                ans %= modVal
        print(ans % modVal)
        return
    
    # convert to absolute value & count zeros
    absNums = []
    zeroCnt = 0
    for i in nums:
        if i == 0:
            zeroCnt += 1
        else:
            absNums.append([abs(i), i])
    absNums.sort()  # sorted by absolute value
    
    # edge case; non-zero cnt is less than k
    if len(absNums) < k:
        print(0)
        return

    # separate non-zero int to 4 sorted lists; all values are absolute value
    posOverK = []
    negOverK = []
    posLessK = []
    negLessK = []
    for _ in range(k):
        temp = absNums.pop()
        if temp[1] > 0:
            posOverK.append(temp[0])
        else:
            negOverK.append(temp[0])
    while absNums:
        temp = absNums.pop()
        if temp[1] > 0:
            posLessK.append(temp[0])
        else:
            negLessK.append(temp[0])

    posOverK.sort()
    negOverK.sort()
    posLessK.sort()
    negLessK.sort()
    
    # odd negative numbers; if able, change to even
    if len(negOverK) % 2:
        minNeg = None
        minPos = None
        maxNeg = None
        maxPos = None
        if posOverK:
            minPos = posOverK[0]
        if negOverK:
            minNeg = negOverK[0]
        if posLessK:
            maxPos = posLessK[-1]
        if negLessK:
            maxNeg = negLessK[-1]
        
        # both case available; pos -> neg or neg -> pos
        if (minNeg and maxPos) and (minPos and maxNeg):
            # compare ratio; use integer comparison, not float
            if maxPos * minPos > maxNeg * minNeg:
                negOverK[0] = maxPos
            else:
                posOverK[0] = maxNeg
        # one case available
        elif not (minNeg and maxPos) and (minPos and maxNeg):
            posOverK[0] = maxNeg
        elif (minNeg and maxPos) and not (minPos and maxNeg):
            negOverK[0] = maxPos
        # unchangable, zero exists
        elif zeroCnt > 0:
            print(0)
            return
    
    # answer building
    ans = 1
    for i in posOverK:
        ans *= i % modVal
        ans = ans % modVal
    for i in negOverK:
        ans *= i % modVal
        ans = ans % modVal
    
    print(ans % modVal)
    return

if __name__ == "__main__":
    main()