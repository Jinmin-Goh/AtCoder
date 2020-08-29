// Contest No.: ABC177
// Problem No.: A
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

int main() {
    int d, t, s;
    scanf("%d %d %d", &d, &t, &s);
    if((double)d / s <= t) {
        printf("Yes");
    }
    else {
        printf("No");
    }
    return 0;
}