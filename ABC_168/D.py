# Contest No.: ABC168
# Problem No.: D
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def main():
    n, m = map(int, input().split())
    graph = {}
    for i in range(n):
        graph[i + 1] = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    stack = [1]
    ans = [None] * (n + 1)
    while stack:
        temp = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for i in graph[node]:
                if ans[i] == None:
                    ans[i] = node
                if i not in visited:
                    temp.append(i)
        stack = temp[:]
    if len(visited) != n:
        print("No")
    else:
        print("Yes")
        for i in range(2, n + 1):
            print(ans[i])
    
    return

if __name__ == "__main__":
    main()