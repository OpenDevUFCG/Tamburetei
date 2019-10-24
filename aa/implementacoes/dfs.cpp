#include <bits/stdc++.h>
#define MAX 1000007

using namespace std;

vector<int> grafo[MAX];
bitset<MAX> vis;

void dfs(int no){
    vis[no] = true;
    for(int i = 0; i < grafo[no].size(); i++){
        if(!vis[grafo[no][i]]){
            dfs(grafo[no][i]);
        }
    }
}
