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

int solve(int N, int Q, vector<int> A) {
  vector<vector<int>> G;
  for (int i = 0; i < N; i++) {
    vector<int> v;
    for (int j = 0; j < N; j++) {
      v.push_back(-1);
    }
    G.push_back(v);
  }
  for (int i = 0; i < N; i++) {
    for (int j = i; j < N; j++) {
      int sweetness = 0;
      for (int r = i; r <= j; r++) {
        sweetness += pow(-1, r - i) * A[r] * (r - i + 1);
      }
      G[i][j] = sweetness;
    }
  }
  int total_sweetness = 0;
  for (int asdf = 0; asdf < Q; asdf++) {
    string a;
    int b, c;
    cin >> a >> b >> c;
    string operation;
    tuple<string, int, int> op = make_tuple(a, b, c);
    int fst;
    int snd;
    tie(operation, fst, snd) = op;
    if (operation == "Q") {
      total_sweetness += G[fst - 1][snd - 1];
    } else {
      A[fst - 1] = snd;
      for (int i = 0; i < N; i++) {
        for (int j = i; j < N; j++) {
          int sweetness = 0;
          for (int r = i; r <= j; r++) {
            sweetness += pow(-1, r - i) * A[r] * (r - i + 1);
          }
          G[i][j] = sweetness;
        }
      }
    }
  }
  return total_sweetness;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, Q;
    cin >> N >> Q;
    vector<int> A;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      A.push_back(x);
    }
    int ans = solve(N, Q, A);
    cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
