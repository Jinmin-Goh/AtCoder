# Contest No.: ABC170
# Problem No.: B
# Solver:      JEMINI
# Date:        20200614

import sys
import heapq

def main():
    a, b = map(int, input().split())
    n, m = 0, 0
    
    n = (4 * a - b)
    m = (b - 2 * a)

    if n < 0 or m < 0 or n % 2 or m % 2:
        print("No")
    else:
        print("Yes")
    
    return

if __name__ == "__main__":
    main()