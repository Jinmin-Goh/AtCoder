# Contest No.: ABC168
# Problem No.: C
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq
import math

def main():
    a, b, h, m = map(int, input().split())
    angle = (math.pi / 30) * m - (m * math.pi / 360 + h * math.pi / 6)
    if angle < 0:
        angle = -angle
    ans = math.sqrt(a * a + b * b - 2 * b * a * math.cos(angle))
    print(ans)
    return

if __name__ == "__main__":
    main()