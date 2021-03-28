#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

// Debug printing
#define watch(x) cout << (#x) << " is " << (x) << endl

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

void reverse(vector<int>& v, int i, int j) {
  reverse(next(v.begin(), i), next(v.begin(), j));
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

  int i = 0, j = 0;
  int p = v.size(), q = v.size();
  int remaining = C - (N - 2);

  while (true) {
    j = min(N - (N - q), remaining);
    reverse(v, i, j);
    remaining -= (j - i);
    i++;

    if (remaining <= 0) {
      break;
    }
    remaining += 1;

    q--;
    p = max(0 + (i - 1), q - remaining - 1);
    reverse(v, p, q);
    remaining -= (q - p);

    if (remaining <= 0) {
      break;
    }
  }

  stringstream ss;
  for (auto it = v.begin(); it != v.end(); it++) {
    ss << *it;
    if (it != v.end()) {
      ss << " ";
    }
  }

  int cost = revsort_cost(v);
  cout << cost << endl;
  // assert(cost == C);
  return ss.str();
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, C;
    cin >> N >> C;
    watch(C);
    string ans = solve(N, C);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
