#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

// Debug printing
#define watch(x) cout << (#x) << " is " << (x) << endl

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

const long long MAX_NUM_ANTS = 100;
const long long MAX_WEIGHT = 500;
int f[MAX_NUM_ANTS][MAX_WEIGHT];

long long solve(int N, vector<int>& w) {
  // int M = 0;
  // for (int i = 0; i < w.size(); i++) {
  //   M += 6 * w[i];
  // }

  for (int i = 0; i <= MAX_NUM_ANTS; i++) {
    for (int j = 0; j <= MAX_WEIGHT; j++) {
      f[i][j] = 0;
    }
  }

  for (int i = 1; i <= MAX_NUM_ANTS; i++) {
    for (int j = 0; j <= MAX_WEIGHT; j++) {
      if (w[i - 1] > j) {
        f[i][j] = f[i - 1][j];
      } else {
        f[i][j] =
            max(f[i - 1][j], 1 + f[i - 1][min(j - w[i - 1], 6 * w[i - 1])]);
      }
      // cout << f[i][j] << endl;
    }
  }

  return f[N][100000];
}

long long calculate_max_possible_weight() {
  const int WI_MAX = 1000000000;
  int num_ants = 0;
  int wi = 1;
  long long total_weight = 0;
  while (wi <= WI_MAX) {
    cout << wi << endl;
    total_weight += wi;
    num_ants += 1;
    while (total_weight > 6 * (long long)wi) {
      wi++;
    }
  }
  cout << "MAX_NUM_ANTS: " << num_ants << endl;
  return total_weight;
}

int main() {
  // long long max_weight = calculate_max_possible_weight();
  // cout << "MAX_WEIGHT: " << max_weight << endl;
  // MAX_NUM_ANTS: 139
  // MAX_WEIGHT: 6994017316
  // return 0;
  cout << "start" << endl;

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<int> w;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      w.push_back(x);
    }
    int ans = solve(N, w);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
