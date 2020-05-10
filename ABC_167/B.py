# Contest No.: ABC167
# Problem No.: B
# Solver:      JEMINI
# Date:        20200510

import sys

def main():
    a, b, c, k = map(int, sys.stdin.readline().split())
    ans = 0
    if k <= a:
        print(k)
        return
    else:
        k -= a
        ans += a
    if k <= b:
        print(ans)
        return
    else:
        k -= b
        print(ans - k)
    return

if __name__ == "__main__":
    main()