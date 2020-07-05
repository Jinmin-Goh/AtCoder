# Contest No.: ABC173
# Problem No.: B
# Solver:      JEMINI
# Date:        20200705

import sys
import heapq

def main():
    n = int(input())
    a, b, c, d = 0, 0, 0, 0

    for i in range(n):
        temp = input()
        if temp == "AC":
            a += 1
        elif temp == "WA":
            b += 1
        elif temp == "TLE":
            c += 1
        else:
            d += 1

    print("AC x", a)
    print("WA x", b)
    print("TLE x", c)
    print("RE x", d)
    return

if __name__ == "__main__":
    main()