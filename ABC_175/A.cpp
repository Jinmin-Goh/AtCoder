// Contest No.: ABC175
// Problem No.: A
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

int main() {
    int cnt = 0;
    char w[3];
    scanf("%s", w);

    if(w[0] == 'R' && w[1] == 'R' && w[2] == 'R') {
        printf("3");
    }
    else if((w[0] == 'R' && w[1] == 'R') || (w[1] == 'R' && w[2] == 'R')) {
        printf("2");
    }
    else if(w[0] == 'S' && w[1] == 'S' && w[2] == 'S') {
        printf("0");
    }
    else {
        printf("1");
    }

    return 0;
}