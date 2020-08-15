// Contest No.: ABC175
// Problem No.: D
// Solver:      Jinmin Goh
// Date:        20200815
 
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
 
long long int pList[5010], cList[5010];
 
int main() {
    long long int n, k;
    scanf("%lld %lld", &n, &k);
 
    for(int i = 1; i <= n; i++) {
        scanf("%lld", &pList[i]);
    }
    for(int i = 1; i <= n; i++) {
        scanf("%lld", &cList[i]);
    }
    long long int ans = -1e15;
 
    for(int i = 1; i <= n; i++) {
        long long int nextPos = pList[i], tempScore = 0;
        long long int tempVal = cList[i];
        for(int j = 0; j < k; j++) {
            tempScore += cList[nextPos];
            //swap(cList[nextPos], tempVal);
            nextPos = pList[nextPos];
            ans = max(ans, tempScore);
        }
    }
 
 
    printf("%lld", ans);
    return 0;
}