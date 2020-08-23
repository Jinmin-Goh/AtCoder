// Contest No.: ABC176
// Problem No.: C
// Solver:      Jinmin Goh
// Date:        20200822

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

int nums[200010];

int main() {
    long long int n, ans = 0;
    scanf("%lld", &n);
    for(int i = 0; i < n; i++) {
        scanf("%lld", &nums[i]);
    }

    int curMin = nums[0];
    for(int i = 0; i < n; i++) {
        if(nums[i] > curMin) {
            curMin = nums[i];
        }
        else {
            ans += curMin - nums[i];
        }
    }
    printf("%lld", ans);
    return 0;
}