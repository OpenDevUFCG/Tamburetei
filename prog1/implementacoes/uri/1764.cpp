// Questão 1764 - Itinerário do Papai Noel
// Link da questão - https://www.beecrowd.com.br/judge/pt/problems/view/1764

#include <bits/stdc++.h>
#include <list>

#define f first
#define s second
#define pb push_back
#define pf pop_front

using namespace std;

const int MAX = 40001;

int onion[MAX];

typedef tuple <int, int, int> ii;

list<ii> liga;

int n, m, a, b, c;

int pai(int num){
    if(num == onion[num]) return num;
    onion[num] = pai(onion[num]);
    return onion[num];
}

void unir(int a, int b){
    onion[onion[b]] = onion[a];
}

void resetar(){
    for(int i = 0; i < MAX; i++)
        onion[i] = i;
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    while(true){
        cin >> n >> m;
        if(n == 0 && m == 0)
            break;
        resetar();

        for(int i = 0; i < m; i++){
            cin >> a >> b >> c;
            liga.pb({c, a, b});
        }

        liga.sort();
        long int ans = 0;

        while(!liga.empty()){
            ii no = liga.front();
            liga.pf();
            if(pai(get<1>(no)) != pai(get<2>(no))){
                ans += get<0>(no);
                unir(get<1>(no), get<2>(no));
            }

        }
        cout << ans << endl;

    }
}