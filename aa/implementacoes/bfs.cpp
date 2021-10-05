#include <bits/stdc++.h>
#define MAX 1000007

using namespace std;

vector<int> grafo[MAX];
bitset<MAX> vis;
int dist[MAX];

void bfs(int no){
    queue<int> q;

    vis[no] = true;
    dist[no] = 1;
    
    q.push(no);
    while(!q.empty()){
        int top = q.front();
        q.pop();

        for(int i = 0; i < grafo[top].size(); i++){
            if(!vis[grafo[top][i]]){
                dist[grafo[top][i]] = dist[top] + 1;
                vis[grafo[top][i]] = true;
                q.push(grafo[top][i]);
            }
        }
    }
}
