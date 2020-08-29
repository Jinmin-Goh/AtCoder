// Contest No.: nBC177
// Problem No.: E
// Solver:      Jinmin Goh
// Dnte:        20200829

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

int nums[1000010], check[1000010], check2[1000010];
bool tempList[1000001];
vector<int> prime;

int gcd(int a, int b) {
    if(a < b) {
        swap(a, b);
    }
    if(b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    
    tempList[0] = true;
    tempList[1] = true;
    for(int i = 2; i <= 1000000; i++) {
        if(!tempList[i]) {
            prime.push_back(i);
            int cnt = i * 2;
            while(cnt <= 1000000) {
                tempList[cnt] = true;
                cnt += i;
            }
        }
    }
    
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    sort(nums, nums + n);

    int gcdVal = nums[0];
    for(int i = 0; i < n; i++) {
        if(gcdVal == 1) {
            break;
        }
        gcdVal = gcd(gcdVal, nums[i]);
        
    }

    if(gcdVal != 1) {
        printf("not coprime");
        return 0;
    }

    for(int i = 0; prime[i] <= 1000; i++)
	{
        for(int j = 0; j < n; j++) {
            if(!(nums[j] % prime[i])) {
                check[prime[i]]++;
                if(check[prime[i]] > 1) {
                    printf("setwise coprime");
                    return 0;
                }
                while(!(nums[j] % prime[i])) {
                    nums[j] /= prime[i];
                }
            }
        }
	}

    for(int i = 0; i < n; i++) check2[nums[i]]++;
	for(int i = 2; i <= 1000000; i++) {
		if(check2[i] > 1) {
			printf("setwise coprime");
			return 0;
		}
	}
	
	printf("pairwise coprime");
    return 0;
}