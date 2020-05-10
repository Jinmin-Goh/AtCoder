# Contest No.: ABC167
# Problem No.: D
# Solver:      JEMINI
# Date:        20200510

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    nums = [None]
    nums += list(map(int, sys.stdin.readline().split()))
    visited = [1]
    visitedSet = set([1])
    temp = nums[1]
    cnt = 0
    while temp not in visitedSet:
        if cnt == k:
            break
        visited.append(temp)
        visitedSet.add(temp)
        temp = nums[temp]
        cnt += 1
    if len(visited) > k:
        print(visited[-1])
        return
    frontCnt = visited.index(temp)
    k -= frontCnt
    cnt = k % (len(visited) - frontCnt)
    print(visited[frontCnt + cnt])
    return

if __name__ == "__main__":
    main()