# Contest No.: ABC171
# Problem No.: C
# Solver:      JEMINI
# Date:        20200621

import sys
import heapq

def main():
    n = int(input())
    ans = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while n > 0:
        ans = alphabet[(n - 1) % 26] + ans
        n = (n - 1) // 26
    print(ans)
    return

if __name__ == "__main__":
    main()