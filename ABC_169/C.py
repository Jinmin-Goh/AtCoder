# Contest No.: ABC169
# Problem No.: C
# Solver:      JEMINI
# Date:        20200531

import sys
import heapq

def main():
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b[:-3] + b[-2:])
    ans = a * b // 100
    print(ans)
    return

if __name__ == "__main__":
    main()