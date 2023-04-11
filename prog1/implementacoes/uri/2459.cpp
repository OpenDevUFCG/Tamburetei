// Questão 2459 - Copa do Mundo
// Link da questão - https://www.beecrowd.com.br/judge/pt/problems/view/2459

#include <bits/stdc++.h>
#include <list>

#define f first
#define s second
#define pb push_back
#define pf pop_front

using namespace std;

const int MAX = 101;

int onion[MAX];

typedef tuple <int, int, int> ii;

list<ii> liga;

int n, f, r, a, b, c;

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

    cin >> n >> f >> r;
    resetar();

    for(int i = 0; i < f; i++){
        cin >> a >> b >> c;
        liga.pb({c, a, b});
    }

    for(int i = 0; i < r; i++){
        cin >> a >> b >> c;
        liga.pb({(c+1000), a, b});
    }

    liga.sort();

    int ans = 0;

    while(!liga.empty()){
        ii no = liga.front();
        liga.pf();
        if(pai(get<1>(no)) != pai(get<2>(no))){
            int custo = get<0>(no);
            if(custo > 1000) custo -= 1000;
            ans += custo;
            unir(get<1>(no), get<2>(no));
        }

    }
    cout << ans << endl;

}