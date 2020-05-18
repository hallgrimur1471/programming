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

int solve(int N, int K, vector<int> A) {
  int next = K;
  int count = 0;
  for (int i = 0; i < N; i++) {
    if (A[i] == K) {
      next = K - 1;
    } else if (A[i] == next) {
      next--;
    } else {
      next = K;
    }
    if (next == 0) {
      count++;
      next = K;
    }
  }
  return count;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, K;
    cin >> N >> K;
    vector<int> A;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      A.push_back(x);
    }
    int ans = solve(N, K, A);
    cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
