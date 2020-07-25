# Contest No.: M-SOLUTIONS Programming Contest 2020
# Problem No.: F
# Solver:      JEMINI
# Date:        20200725

import sys
import heapq

def main():
    n = int(input())
    XUList = []
    #YUList = []
    XRList = []
    #YRList = []
    XDList = []
    #YDList = []
    XLList = []
    #YLList = []

    for _ in range(n):
        x, y, d = sys.stdin.readline().split()
        x, y = int(x), int(y)
        if d == "U":
            XUList.append((x, y))
            #YUList.append((y, x))
        elif d == "R":
            XRList.append((x, y))
            #YRList.append((y, x))
        elif d == "D":
            XDList.append((x, y))
            #YDList.append((y, x))
        else:
            XLList.append((x, y))
            #YLList.append((y, x))

    XUList.sort()
    #YUList.sort()
    XRList.sort()
    #YRList.sort()
    XDList.sort()
    #YDList.sort()
    XLList.sort()
    #YLList.sort()
    #print(XUList, XRList, XDList, XLList)
    ans = 10 ** 9
    for UPlane in XUList:
        for RPlane in XRList:
            if UPlane[0] > RPlane[0] and UPlane[1] < RPlane[1] and UPlane[0] - RPlane[0] == RPlane[1] - UPlane[1]:
                ans = min(ans, (RPlane[1] - UPlane[1]) * 10)
        for DPlane in XDList:
            if UPlane[0] == DPlane[0] and UPlane[1] < DPlane[1]:
                ans = min(ans, abs(UPlane[1] - DPlane[1]) * 5)
        for LPlane in XLList:
            if UPlane[0] < LPlane[0] and UPlane[1] < LPlane[1] and LPlane[0] - UPlane[0] == LPlane[1] - UPlane[1]:
                ans = min(ans, (LPlane[1] - UPlane[1]) * 10)
    
    for DPlane in XDList:
        for RPlane in XRList:
            if DPlane[0] > RPlane[0] and DPlane[1] > RPlane[1] and DPlane[0] - RPlane[0] == DPlane[1] - RPlane[1]:
                ans = min(ans, (DPlane[1] - RPlane[1]) * 10)
        for LPlane in XLList:
            if DPlane[0] < LPlane[0] and DPlane[1] > LPlane[1] and LPlane[0] - DPlane[0] == DPlane[1] - LPlane[1]:
                ans = min(ans, (DPlane[1] - LPlane[1]) * 10)
            
    for RPlane in XRList:
        for LPlane in XLList:
            if RPlane[1] == LPlane[1] and RPlane[0] < LPlane[0]:
                ans = min(ans, (LPlane[0] - RPlane[0]) * 5)
    if ans == 10 ** 9:
        print("SAFE")
    else:
        print(ans)
    return

if __name__ == "__main__":
    main()