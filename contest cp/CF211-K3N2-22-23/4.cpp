#include <bits/stdc++.h>
using namespace std;

#define int long long


signed main() {
   // freopen("input.txt","r", stdin);
    
    int n; cin >> n;
    int t[n+1], r[n+1];
    for(int i = 1; i <= n; ++i) 
        cin >> t[i];
    for(int i = 1; i <= n; ++i) 
        cin >> r[i];
    int f[n+1];
    f[0] = 0;
    f[1] = t[1];

    for(int i = 2; i <= n; ++i) 
        f[i] = min(f[i-1]+t[i], f[i-2] + r[i-1]);

    cout << f[n];

}