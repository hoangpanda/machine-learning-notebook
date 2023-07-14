#include <bits/stdc++.h>
using namespace std;

#define int long long

const int mod = 1e9 + 7;
int sqr(int n) {
    return n*n;
}

int cal(int a, int b) // a^b
{
    if(b == 0) return 1;
    if(b % 2 == 0) 
        return sqr(cal(a,b/2)%mod)%mod;
    return (a%mod)*(sqr(cal(a,b/2)%mod)%mod)%mod;
} 

int f(int n) {
    return n - 2;
} 

signed main() {
  //  freopen("input.txt","r", stdin);
    int a,r,m,n;
    cin >> a >> r >> n >> m;
    
    int ans = 0;
    a %= mod;


    int x1 = cal(r,m);
    int x2 = cal(r,n);
    int k = (cal(r, m) - cal(r,n) + mod)%mod;
    //cout << x1 << endl;
    //cout << x2 << endl;

    int b = cal(r-1, f(mod));

    a = (a*k)%mod;

    cout << (a*b)%mod;

}
