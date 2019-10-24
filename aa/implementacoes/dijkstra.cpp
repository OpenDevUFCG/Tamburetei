#include <bits/stdc++.h>
#define MAX 10000007
#define INF 100000007

using namespace std;

typedef pair<int,int> di;

vector<di>grafo[MAX];
int dist[MAX], n, m;//different of BFS --> (vis[MAX])

void star(int no){
    priority_queue<di, vector<di>, greater<di> > fila; //different of BFS --> (queue<di> fila)

    dist[no] = 0;
    fila.push(make_pair(0, no));
    while(!fila.empty()){
        di top = fila.top();
        fila.pop();

        int peso = top.first;
        int v = top.second;
        if(dist[v] < peso) continue; //different of BFS
        for(int i = 0; i < grafo[v].size(); i++){
            di vizinho = grafo[v][i];
            if(dist[vizinho.second] > dist[v] + vizinho.first){ //different of BFS --> (!vis[grafo[v][i]])
                dist[vizinho.second] = dist[v] + vizinho.first;
                fila.push(make_pair(dist[vizinho.second], vizinho.second));
            }
        }
    }
}

int main(){
    scanf("%d %d", &n, &m);
    for(int i = 0; i <= n; i++) dist[i] = INF;

    for(int i = 0; i < m; i++){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        grafo[a].push_back(make_pair(c, b));
        grafo[b].push_back(make_pair(c, a));
    }
    star(n);
    return 0;
}
