# Contest No.: M-SOLUTIONS Programming Contest 2020
# Problem No.: D
# Solver:      JEMINI
# Date:        20200725

import sys
import heapq

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))

    money = 1000
    stock = 0
    minVal = nums[0]
    maxVal = nums[0]

    if n == 2:
        if nums[0] < nums[1]:
            money = 1000 - (1000 // nums[0]) * nums[0]
            stock = (1000 // nums[0])

            print(money + stock * nums[1])
        else:
            print(1000)
        return

    upFlag = False
    downFlag = False
    # if nums[0] < nums[1]:
    #     upFlag = True
    
    # elif nums[0] > nums[1]:
    #     downFlag = True
    money = 1000
    stock = 0
    for i in range(n - 1):
        # print(upFlag, downFlag)
        # print(money, stock)
        # local minimum
        if nums[i] < nums[i + 1]:
            if upFlag:
                continue
            else:
                # buy
                tempStock = money // nums[i]
                stock += tempStock
                money -= tempStock * nums[i]
                downFlag = False
                upFlag = True
        # local maximum
        if nums[i] > nums[i + 1]:
            if downFlag:
                continue
            else:
                # sell
                money += stock * nums[i]
                stock = 0
                downFlag = True
                upFlag = False
        # print(upFlag, downFlag)
        # print(money, stock)
    


    if stock:
        money += stock * nums[-1]

    print(money)
    return

if __name__ == "__main__":
    main()