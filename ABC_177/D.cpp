// Contest No.: ABC177
// Problem No.: D
// Solver:      Jinmin Goh
// Date:        20200829

#include <cstring>
#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int AList[200010], BList[200010], parent[200010], parentCnt[200010];

int findParent(int node) {
    if(parent[node] == node) {
        return node;
    }
    parent[node] = findParent(parent[node]);
    return parent[node];
}

void unionFunc(int node1, int node2) {
    int p1 = findParent(node1), p2 = findParent(node2);
    parent[p2] = p1;
    return;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    for(int i = 0; i < m; i++) {
        scanf("%d %d", &AList[i], &BList[i]);
        unionFunc(AList[i], BList[i]);
    }

    for(int i = 1; i <= n; i++) {
        parentCnt[findParent(i)]++;
    }

    int ans = 0;
    for(int i = 1; i <= n; i++) {
        ans = max(ans, parentCnt[i]);
    }
    printf("%d", ans);
    return 0;
}