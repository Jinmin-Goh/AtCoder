# Contest No.: ABC167
# Problem No.: A
# Solver:      JEMINI
# Date:        20200510

import sys

def main():
    s = input()
    t = input()
    ans = True
    for i in range(len(s)):
        if s[i] != t[i]:
            ans = False
            break
    if ans:
        print("Yes")
    else:
        print("No")
    return

if __name__ == "__main__":
    main()