#include <bits/stdc++.h>
#define MAX 100

using namespace std;


bitset<MAX> primes;
void sieve(){
    primes.set();
    primes[0] = primes[1] = 0;

    for(long long int i = 2; i < MAX; i++){
        if(primes[i]){
            for(long long int j = i*i; j < MAX; j += i) primes[j] = 0;
            //printf("%lld ", i);
        }
    }
}
int main(){
    sieve();
    return 0;
}
