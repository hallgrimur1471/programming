#include <bits/stdc++.h>

using namespace std;

#define watch(x) cout << (#x) << " is " << (x) << endl

#define OPI(v)                                                                 \
  for (auto e : v) {                                                           \
    cout << e << " ";                                                          \
  }                                                                            \
  cout << "\n";

#define EPI(v)                                                                 \
  for (auto e : v) {                                                           \
    cerr << e << " ";                                                          \
  }                                                                            \
  cerr << "\n";

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

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    map<int, int> cs;
    for (int i = 0; i < ((2 * N - 1) * N); i++) {
      int a;
      cin >> a;
      if (cs.find(a) != cs.end()) {
        cs[a]++;
      } else {
        cs[a] = 1;
      }
    }
    cout << "Case #" << t << ":";
    for (auto c : cs) {
      if (c.second % 2 != 0) {
        cout << " " << c.first;
      }
    }
    cout << "\n";
  }
  return 0;
}
