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
} // namespace std

mt19937 rng(1234);

int MAX_INT = 2147483647;

string solve(int X, int Y, string M) {
  pair<int, int> a = make_pair(X, Y);
  int a_traveled = 0;
  int mn = MAX_INT;
  for (int i = 0; i < M.size(); i++) {
    int b_travel = abs(a.first) + abs(a.second);
    if (b_travel <= a_traveled) {
      if (a_traveled < mn) {
        mn = a_traveled;
      }
    }
    if (M[i] == 'S') {
      a = make_pair(a.first, a.second - 1);
    } else if (M[i] == 'E') {
      a = make_pair(a.first + 1, a.second);
    } else if (M[i] == 'N') {
      a = make_pair(a.first, a.second + 1);
    } else if (M[i] == 'W') {
      a = make_pair(a.first - 1, a.second);
    }
    a_traveled++;
  }
  int b_travel = abs(a.first) + abs(a.second);
  if (b_travel <= a_traveled) {
    if (a_traveled < mn) {
      mn = a_traveled;
    }
  }
  if (mn == MAX_INT) {
    return "IMPOSSIBLE";
  }
  return to_string(mn);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int X, Y;
    string M;
    cin >> X >> Y;
    cin >> M;
    string ans = solve(X, Y, M);
    cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
