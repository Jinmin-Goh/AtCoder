# Contest No.: ABC173
# Problem No.: A
# Solver:      JEMINI
# Date:        20200705

import sys
import heapq

def main():
    n = int(input())
    print((1000 - n % 1000) % 1000)
    return

if __name__ == "__main__":
    main()