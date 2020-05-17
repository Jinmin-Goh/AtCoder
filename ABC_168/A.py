# Contest No.: ABC168
# Problem No.: A
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")
    return

if __name__ == "__main__":
    main()