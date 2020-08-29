// Contest No.: ABC177
// Problem No.: B
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

int nums[100010];

int main() {
    char s[1010], t[1010];
    scanf("%s", s);
    scanf("%s", t);
    int maxVal = 0;
    for(int i = 0; i < strlen(s) - strlen(t) + 1; i++) {
        int tempVal = 0;
        for(int j = 0; j < strlen(t); j++) {
            if(s[i + j] == t[j]) {
                tempVal++;
            }
        }
        maxVal = max(maxVal, tempVal);
    }
    printf("%ld", strlen(t) - maxVal);
    return 0;
}