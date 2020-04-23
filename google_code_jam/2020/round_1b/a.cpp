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

void solve() {}

void populate_help(unordered_map<pair<int, int>, string> &m, pair<int, int> pos, int power, string story) {
  if (abs(pos.first) > pow(10, 1) || abs(pos.second) > pow(10, 1)) {
    return;
  }
  for (auto c: "NESW") {
    pair<int, int> pos_original = pos;
    if (c == 'N') {
      pos.second += power;
    }
    else if (c == 'E') {
      pos.first += power;
    }
    else if (c == 'S') {
      pos.second -= power;
    }
    else if (c == 'W') {
      pos.first -= power;
    }
    //cerr << m.size() << endl;
    //cerr << pos.first << ":" << pos.second << endl;;
    if (m.find(pos) != m.end()) {
    }
    else {
      m[pos] = (story + c);
      populate_help(m, pos, 2*power, story + c);
    }
    pos = pos_original;
  }
}

void populate(unordered_map<pair<int, int>, string> &m) {
  int power = 1;
  string story = "";
  pair<int, int> pos = make_pair(0, 0);
  populate_help(m, pos, power, story);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  unordered_map<pair<int, int>, string> m;
  populate(m);
  for (auto e: m) {
    cerr << e.first.first << " " << e.first.second << " -> " << e.second << "\n";
  }
  for (int t = 1; t <= T; t++) {
    int X, Y;
    cin >> X >> Y;
    pair<int, int> p = make_pair(X, Y);
    if (m.find(p) == m.end()) {
      cout << "Case #" << t << ": " << "IMPOSSIBLE" << "\n";
    }
    else {
      cout << "Case #" << t << ": " << m[p] << "\n";
    }
  }
  return 0;
}

