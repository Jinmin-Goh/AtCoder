// Contest No.: ABC176
// Problem No.: A
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

int nums[100010];

int main() {
    int n, x, t, ans;
    scanf("%d %d %d", &n, &x, &t);

    printf("%d", ((n + x - 1) / x) * t);

    return 0;
}