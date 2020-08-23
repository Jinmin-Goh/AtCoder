// Contest No.: ABC176
// Problem No.: D
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

int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1},
    ddx[25] = {-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2},
    ddy[25] = {-2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -1, 0, 1, 2};
char mapTable[1010][1010];


int main() {
    int h, w, Ch, Dh, Cw, Dw;
    scanf("%d %d", &h, &w);
    scanf("%d %d", &Ch, &Cw);
    scanf("%d %d", &Dh, &Dw);
    for(int i = 0; i < h; i++) {
        scanf("%s", mapTable[i]);
    }
    pair<int, int> start = {Ch - 1, Cw - 1};
    queue<pair<int, int>> queueList, adjList;
    queueList.push(start);

    bool flag;
    int cnt = 0;
    while(queueList.size()) {
        flag = false;
        
        while(queueList.size()) {
            queueList.push(make_pair(-1, -1));
            while(true) {
                pair<int, int> temp = queueList.front();
                queueList.pop();
                //printf("%d %d\n", temp.first, temp.second);
                if(temp.first == -1 && temp.second == -1) {
                    break;
                }
                if(temp.first == Dh - 1 && temp.second == Dw - 1) {
                    flag = true;
                    break;
                }
                if(mapTable[temp.first][temp.second] == '*' || mapTable[temp.first][temp.second] == '#') {
                    continue;
                }
                mapTable[temp.first][temp.second] = '*';
                int x = temp.first, y = temp.second;
                for(int i = 0; i < 4; i++) {
                    if(x + dx[i] >= 0 && x + dx[i] < h && y + dy[i] >= 0 && y + dy[i] < w && mapTable[x + dx[i]][y + dy[i]] == '#') {
                        adjList.push(make_pair(x, y));
                    }
                    if(x + dx[i] >= 0 && x + dx[i] < h && y + dy[i] >= 0 && y + dy[i] < w && mapTable[x + dx[i]][y + dy[i]] != '*' && mapTable[x + dx[i]][y + dy[i]] != '#') {
                        queueList.push(make_pair(x + dx[i], y + dy[i]));
                    }
                }
                
            }
            if(flag) {
                break;
            }
        }
        if(flag) {
            break;
        }
        while(adjList.size()) {
            pair<int, int> temp = adjList.front();
            adjList.pop();
            int x = temp.first, y = temp.second;
            for(int i = 0; i < 25; i++) {
                if(x + ddx[i] >= 0 && x + ddx[i] < h && y + ddy[i] >= 0 && y + ddy[i] < w && mapTable[x + ddx[i]][y + ddy[i]] != '*' && mapTable[x + ddx[i]][y + ddy[i]] != '#') {
                    queueList.push(make_pair(x + ddx[i], y + ddy[i]));
                }
            }
        }
        cnt++;

    }

    if(flag) {
        printf("%d", cnt);
    }
    else {
        printf("-1");
    }

    return 0;
}