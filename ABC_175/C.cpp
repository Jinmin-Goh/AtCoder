// Contest No.: ABC175
// Problem No.: C
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

int nums[200010];

int main() {
    long long int x, k, d;
    scanf("%lld %lld %lld", &x, &k, &d);
    if(x < 0) x = -x;

    //printf("%lld %lld %lld\n", d, x, k);

    long long int divVal = x / d, ans = 0;
    if(k <= divVal) {
        ans = x - k * d;
    }
    else {
        k -= divVal;
        x -= divVal * d;
        //printf("%lld %lld %lld\n", divVal, x, k);
        if(k % 2) {
            x -= d;
        }
        ans = abs(x);
    }

    printf("%lld", ans);
    return 0;
}