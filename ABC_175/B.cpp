// Contest No.: ABC175
// Problem No.: B
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

int nums[110];
map<int, int> mappingList;
vector<int> uniqueList;

int main() {
    int n;
    scanf("%d", &n);
    if(n < 3) {
        printf("0");
        return 0;
    }
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    //sort(nums, nums + n);

    

    int ans = 0;
    for(int i = 0; i < n - 2; i++) {
	    for(int j = i + 1; j < n - 1; j++) {
            for(int k = j + 1; k < n; k++) {
                if((nums[i] != nums[j]) && (nums[k] != nums[j]) && (nums[i] != nums[k]) && (nums[i] + nums[j] > nums[k]) && (nums[i] + nums[k] > nums[j]) && (nums[k] + nums[j] > nums[i])) {
                    ans++;
                }
            }
        }
    }

    printf("%d", ans);
    return 0;
}