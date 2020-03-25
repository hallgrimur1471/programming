#include <bits/stdc++.h>

using namespace std;

#define watch(x) cout << (#x) << " is " << (x) << endl

typedef long long ll;
typedef pair<int, int> ipair;

// inject to std how to hash a pair of ints
namespace std {
template <> struct hash<pair<int, int>> {
  size_t operator()(pair<int, int> const &p) const noexcept {
    return hash<int>()(p.first) ^ hash<int>()(p.second);
  }
};
}

mt19937 rng(1234);

void solve() {}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
  return 0;
}
