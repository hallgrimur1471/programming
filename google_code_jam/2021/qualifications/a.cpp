#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

int solve(vector<int> v) {
  int cost = 0;
  for (auto it = v.begin(); it != prev(v.end()); it++) {
    auto min_it = min_element(it, v.end());
    int dist = distance(it, min_it) + 1;
    cost += dist;
    reverse(it, next(min_it));
  }
  return cost;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<int> v;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      v.push_back(x);
    }
    int ans = solve(v);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
