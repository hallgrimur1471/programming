#include <bits/stdc++.h>

using namespace std;

#define watch(x) cerr << (#x) << " is " << (x) << endl

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

void solve(int R, int S, int t) {
  vector<int> a;
  for (int i = 0; i < S; i++) {
    for (int j = 0; j < R; j++) {
      a.push_back(j+1);
    }
  }
  EPI(a);
  vector<pair<int, int>> sol;
  while (true) {
    int i = 0;
    int a_i = i;
    int f = a[i];
    i++;
    while (a[i] >= a[i-1]) {
      i++;
    }
    int a_j = i;
    int s = a[i-1];
    int b_i = a_j;
    while (a[i] != s) {
      i++;
    }
    int b_j = i;
    vector<int> v;
    for (int i = b_i; i < b_j; i++) {
      v.push_back(a[i]);
    }
    for (int i = a_i; i < a_j; i++) {
      v.push_back(a[i]);
    }
    for (int i = b_j; i < a.size(); i++) {
      v.push_back(a[i]);
    }
    a = v;
    EPI(a);
    bool sorted = true;
    for (int i = 1; i < a.size(); i++) {
      if (a[i] < a[i-1]) {
        sorted = false;
        break;
      }
    }
    sol.push_back(make_pair(a_j - a_i, b_j - b_i));
    if (sorted) {
      cerr << "sorted" << endl;
      break;
    }
  }
  cout << "Case #" << t << ": " << sol.size() << "\n";
  for (auto p: sol) {
    cout << p.first << " " << p.second << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int R, S;
    cin >> R >> S;
    watch(R); watch(S);
    solve(R, S, t);
  }
  return 0;
}

