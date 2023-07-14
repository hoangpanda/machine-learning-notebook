#include <bits/stdc++.h>
using namespace std;

#define int long long


int n;
const int N = 1e5 + 1;
int parent[N];
int ss[N];

int find_parent(int a) {
    if(parent[a] == a) {
        return a;
    }
    return parent[a] = find_parent(parent[a]);
}

signed main() {
  //  freopen("input.txt","r", stdin);
    
    cin >> n;
    map<string, int> mp;
    pair<string, string> p[n+1];
    int idx = 0;
    for(int i = 1; i <= n; ++i) {
        string a,b; cin >> a >> b;
        p[i] = {a,b};
        if(mp[a] == 0) {
            idx++;
            mp[a] = idx;
        } 
        if(mp[b] == 0) {
            idx++;
            mp[b] = idx;
        }
    }

    //cout << mp["Toan"] << endl;

    for(int i = 1; i <= 1e5; ++i) {
        parent[i] = i;
        ss[i] = 1;
    }

    for(int i = 1; i <= n; ++i) {
        string a = p[i].first;
        string b = p[i].second;
        //cout << "two str:" << a << ' ' << b << endl;

        int idx_a = mp[a];
        int idx_b = mp[b];
        //cout <<"two label: "<< idx_a << ' ' << idx_b << endl;
        idx_a = find_parent(idx_a);
        idx_b = find_parent(idx_b);
        //cout << "two parent: " << idx_a << ' ' << idx_b << endl;
        if(idx_a != idx_b) {
            if(ss[idx_a] >= ss[idx_b]) {
                //cout << idx_b << "is parent of " << idx_a << endl;
                parent[idx_b] = idx_a;
                ss[idx_a] += ss[idx_b];
                cout <<  ss[idx_a] << endl;
            }
            else {
                parent[idx_a] = idx_b;
                ss[idx_b] += ss[idx_a];
                cout  << ss[idx_b] << endl;
            }
        }
        else {
            cout << ss[idx_a] << endl;
        }
    }

}