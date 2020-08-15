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

long long int pList[5010], cList[5010], visited[5010], position[5010];
pair<long long, long long> cycleData[5010];

int main() {
    long long int n, k;
    scanf("%lld %lld", &n, &k);

    for(int i = 1; i <= n; i++) {
        scanf("%lld", &pList[i]);
    }
    for(int i = 1; i <= n; i++) {
        scanf("%lld", &cList[i]);
    }
    int cnt = 1;
    long long int ans = -1e15;
    for(int i = 1; i <= n; i++) {
        if(visited[i]) continue;
        int start = i, nextVal = pList[i], tempCnt = 0, tempSum = 0;
        
        position[i] += cnt;
        visited[nextVal] = 1;
        cycleData[cnt].first += cList[nextVal];
        cycleData[cnt].second++;
        
        while(start != nextVal) {
            //printf("%d %d\n", nextVal, cnt);
            position[nextVal] += cnt;
            nextVal = pList[nextVal];
            visited[nextVal] = 1;
            cycleData[cnt].first += cList[nextVal];
            cycleData[cnt].second++;
        }
        cnt++;
    }

    for(int i = 1; i <= n; i++) {
        
        long long int nextPos = pList[i], tempScore = 0;
        long long int tempVal = cList[i], newScore = 0;
        int tempk = k;
        if(tempk > cycleData[position[i]].second) {
            tempScore += (tempk / cycleData[position[i]].second) * cycleData[position[i]].first;
            tempk %= cycleData[position[i]].second;
        }

        for(int j = 0; j < tempk; j++) {
            tempScore += cList[nextPos];
            newScore += cList[nextPos];
            //swap(cList[nextPos], tempVal);
            nextPos = pList[nextPos];
            ans = max(ans, tempScore);
            ans = max(ans, newScore);
        }
    }


    printf("%lld", ans);
    return 0;
}