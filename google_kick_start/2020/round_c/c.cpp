#include <bits/stdc++.h>
#include <cmath>

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

int solve(int N, vector<int> &A, unordered_set<int> &perfect) {
  vector<int> curr;
  int count = 0;
  for (int i = 0; i < N; i++) {
    for (int k = 0; k < curr.size(); k++) {
      curr[k] += A[i];
      if (perfect.find(curr[k]) != perfect.end()) {
        count++;
      }
    }
    curr.push_back(A[i]);
    if (perfect.find(A[i]) != perfect.end()) {
      count++;
    }
  }
  return count;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  unordered_set<int> perfect;
  int i = 0;
  while (true) {
    if (i * i > 10000000) {
      break;
    }
    perfect.insert(i * i);
    i++;
  }
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<int> A;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      A.push_back(x);
    }
    int ans = solve(N, A, perfect);
    cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
