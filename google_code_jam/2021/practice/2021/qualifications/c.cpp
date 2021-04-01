

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

// Vector to string:
// {1, 2, 3} -> "1 2 3"
template <typename T>
string v2s(vector<T> v) {
  ostringstream ss;
  for (auto it = v.begin(); it != v.end(); it++) {
    ss << *it;
    if (it != prev(v.end())) {
      ss << " ";
    }
  }
  return ss.str();
}

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

bool is_possible(int N, int C) {
  return ((N - 1 <= C) && (C <= (((N * (N + 1)) / 2) - 1)));
}

vector<int> create_revsort_vector(int N, int C) {
  if (N == 1) {
    assert(C == 0);
    return (vector<int>){1};
  }

  // Since is_possible(N, C) == True
  // current_iteration_cost must have at least
  // one possible value somewhere between 1 and N inclusive.
  int current_iteration_cost = 1;
  while (!is_possible(N - 1, C - current_iteration_cost)) {
    current_iteration_cost++;
  }

  vector<int> v = create_revsort_vector(N - 1, C - current_iteration_cost);

  for (int i = 0; i < v.size(); i++) {
    v[i]++;
  }

  reverse(v.begin(), next(v.begin(), current_iteration_cost - 1));
  v.insert(next(v.begin(), current_iteration_cost - 1), 1);

  return v;
}

string solve(int N, int C) {
  if (!is_possible(N, C)) {
    return "IMPOSSIBLE";
  }

  vector<int> v = create_revsort_vector(N, C);
  assert(revsort_cost(v) == C);
  return v2s(v);
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
