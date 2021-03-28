#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

int revsort_cost(vector<int> v) {
  int cost = 0;
  for (auto it = v.begin(); it != prev(v.end()); it++) {
    auto min_it = min_element(it, v.end());
    int dist = distance(it, min_it) + 1;
    cost += dist;
    reverse(it, next(min_it));
  }
  return cost;
}

string solve(int N, int C) {
  if (C < N - 1) {
    return "IMPOSSIBLE";
  }
  if (C > (((N * (N + 1)) / 2) - 1)) {
    return "IMPOSSIBLE";
  }

  vector<int> v(N, 0);
  iota(v.begin(), v.end(), 1);

  random_device rd;
  mt19937 gen{rd()};
  while (revsort_cost(v) != C) {
    shuffle(v.begin(), v.end(), gen);
  }

  ostringstream s;
  for (auto it = v.begin(); it != v.end(); it++) {
    s << (*it);
    if (it != prev(v.end())) {
      s << " ";
    }
  }
  return s.str();
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, C;
    cin >> N >> C;
    string ans = solve(N, C);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
