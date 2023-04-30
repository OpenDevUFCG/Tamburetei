// Questão 1148 - Países em Guerra
// Link da questão - https://www.beecrowd.com.br/judge/pt/problems/view/1148

#include <bits/stdc++.h>
#include <list>

#define f first
#define s second
#define pb push_back

using namespace std;

const int MAX = 501;
const int inf = 10000000;

int n, m, a, b, h, r, ans;

typedef pair<int, int> ii;

int valores[MAX][MAX];
list<int> grafo[MAX];

int bfs(int no, int cheg){

	int dist[MAX];
	bool mark[MAX];

	for (int i = 1; i <= n; i++)
		dist[i] = inf;

    for (int i = 1; i <= n; i++)
		mark[i] = false;

	priority_queue<ii, vector<ii>, greater<ii>> fila;

	fila.push({0, no});
	dist[no] = 0;

	while(!fila.empty()){

		int k = fila.top().s;
		fila.pop();

		if(mark[k]){
			continue;
		}

		mark[k] = true;

		for(int v: grafo[k]){

			int w = valores[k][v];
			if(dist[v] > dist[k] + w){
				dist[v] = dist[k] + w;
				fila.push({dist[v], v});

			}
		}
	}

	return dist[cheg];
}

void resetar(){
	for (int i = 1; i < MAX; i++)
        grafo[i] = {};

	for (int i = 1; i < MAX; i++)
		for (int j = 1; j < MAX; j++)
			valores[i][j] = inf;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
 	while (true){
		cin >> n >> m;
		if(n == m && n == 0)
			break;

		resetar();
		for (int i = 0; i < m; ++i)
		{
			cin>>a>>b>>h;
			grafo[a].pb(b);
			if(valores[b][a] != inf){
				valores[a][b] = 0;
				valores[b][a] = 0;
			} else {
				valores[a][b] = h;
			}
		}
		cin>>r;
		for (int i = 0; i < r; ++i)
		{
			cin>>a>>b;
			ans = bfs(a, b);
			if (ans < inf) {
				cout<<ans<<endl;
			} else {
				cout<<"Nao e possivel entregar a carta"<<endl;
			}
		}
		cout<<endl;

	}

	return 0;

}