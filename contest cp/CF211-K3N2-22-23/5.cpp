#include <bits/stdc++.h>
using namespace std;

#define int long long


int search(int a, int b, int k) {
    // a <= x^k <= b
    float aa = pow(float(a),1/(float)(k));
    float bb = pow(float(b),1/(float)(k));
    for(int i = aa; i <= bb; ++i)
        if(pow(i,k) >= a && pow(i,k) <= b) return true;
    return false;
}

void test_case(int cnt) {
    double aa,bb; cin >> aa >> bb;
    int a = (int)aa;
    int b = (int)bb;
    //cout << a <<' ' << b << endl;
    // k = 1 -> 39
    int ans = 1;
    for(int i = 1; i <= 39; ++i) {
        if(search(a,b,i)) 
            ans = i;
    }
    cout << "C #" << cnt << ": " << ans << endl;
}

signed main() {
  //  freopen("input.txt","r", stdin);
    
    int t; cin >> t;
    int cnt = 0;
    while(t--) {
        cnt++;
        test_case(cnt);
    }

}