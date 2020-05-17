# Contest No.: ABC168
# Problem No.: B
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)
    return

if __name__ == "__main__":
    main()