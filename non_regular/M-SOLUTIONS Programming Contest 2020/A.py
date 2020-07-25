# Contest No.: M-SOLUTIONS Programming Contest 2020
# Problem No.: A
# Solver:      JEMINI
# Date:        20200725

import sys
import heapq

def main():
    n = int(input())
    if 400 <= n < 600:
        print(8)
    elif 600 <= n < 800:
        print(7)
    elif 800 <= n < 1000:
        print(6)
    elif 1000 <= n < 1200:
        print(5)
    elif 1200 <= n < 1400:
        print(4)
    elif 1400 <= n < 1600:
        print(3)
    elif 1600 <= n < 1800:
        print(2)
    elif 1800 <= n < 2000:
        print(1)
    return

if __name__ == "__main__":
    main()