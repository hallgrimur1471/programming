#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>
#include <numeric>

using namespace std;

#define ll long long
#define N (ll)(1e6+3)
#define INF (ll)(1e18+1)
#define EPS (1e-8)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pdd pair<ld,ld>
#define fi first
#define se second
#define rep(i,a,n) for (ll i = a; i<n; i++)
#define per(i,a,n) for (ll i = n-1; i>=a; i--)
#define pb push_back

ll g[100];
ll r[100][100];
pair<ll,ll> bounds[100][100];
bool used[100][100];
set<ll> sizes;

void solve() {
    memset(used, 0, sizeof(used));
    sizes = set<ll>();

    ll n, p;
    cin >> n >> p;
    rep(i,0,n) {
        cin >> g[i];
    }
    rep(i,0,n) {
        rep(j,0,p) {
            cin >> r[i][j];
        }
        sort(&r[i][0], &r[i][p]);
    }

    rep(i,0,n) {
        rep(j,0,p) {   
            ll high = (ll)floor(r[i][j]/0.9);
            ll low = (ll)ceil(r[i][j]/1.1);
            high = high/g[i];
            low = (low+g[i]-1)/g[i];
            bounds[i][j] = {high,low};
            sizes.insert(high);
            sizes.insert(low);
        }

    }

    ll ans = 0;
    for(auto sz: sizes) {
        while(true) {
            vector<pair<ll,ll> > kit;
            bool bad = false;
            rep(i,0,n) {
                bool found = false;
                rep(j,0,p) {
                    if (!used[i][j] && sz >= bounds[i][j].second && sz <= bounds[i][j].first) {
                        kit.push_back({i,j});
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    bad = true;
                    break;
                }
            }
            if (bad) break;
            ans++;
            for (auto aa : kit) {
                used[aa.first][aa.second] = true;
            }
        }
    }

    cout << ans << endl;
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll t;
    cin >> t;
    rep(i,0,t) {
       cout << "Case #" << i+1 << ": ";
       solve();
    }
}