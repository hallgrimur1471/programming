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

#define EMAP(M)                                                                \
  cerr << (#M) << " is:\n";                                                    \
  for (auto m : M) {                                                           \
    cerr << m.first << " -> " << m.second << "\n";                             \
  }

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

int solve(int N, vector<int> W) {
  // TODO: change map to unordered_map to improve time
  map<int, int> M;
  M[0] = 0;
  for (int i = 0; i < N; i++) {
    // watch(W[i]);
    int size = M.size();
    // watch(size);
    for (int j = size - 1; j >= 0; j--) {
      auto m = M[j];
      // cerr << j << " -> " << M[j] << "\n";
      if (M[j] <= W[i] * 6) {
        if (M.find(j + 1) == M.end() || M[j + 1] > M[j] + W[i]) {
          M[j + 1] = M[j] + W[i];
        }
      }
    }
    // EMAP(M);
  }
  auto it = M.end();
  it--;
  return (*it).first;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    watch(N);
    vector<int> W;
    cerr << "W: ";
    for (int i = 0; i < N; i++) {
      int w;
      cin >> w;
      cerr << w << " ";
      W.push_back(w);
    }
    cerr << "\n";
    int ans = solve(N, W);
    cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
