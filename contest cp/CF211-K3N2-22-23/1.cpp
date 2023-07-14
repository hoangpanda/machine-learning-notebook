#include <bits/stdc++.h>
using namespace std;

#define int long long


signed main() {
   // freopen("input.txt","r", stdin);
    int n,m; cin >> n >> m;
    pair<int,int> p[m];
    int cnt = n;
    int ans = 0;
    for(int i = 0; i < m; ++i) {
        cin >> p[i].second >> p[i].first;    
    }

    for(int i = 0; i < m; ++i)
        for(int j = i+1; j < m; ++j)
            if(p[i].first < p[j].first) 
                swap(p[i], p[j]);

    for(int i = 0; i < m; ++i) {
        if(cnt >= p[i].second) {
            cnt -= p[i].second;
            ans += p[i].first*p[i].second;
        }
        else {
            ans += p[i].first*cnt;    
            break;
        }
    }

    cout << ans;
}