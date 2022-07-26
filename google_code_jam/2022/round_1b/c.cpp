#include <bits/stdc++.h>
#include <random>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

void solve() {
  int num_exchanges = 0;
  string s = "11111111";
  cout << s << endl;
  int N;
  cin >> N;
  if (N == -1) {
    exit(1);
  }
  if (N == 0) {
    return;
  }
  num_exchanges++;
  while (num_exchanges < 300) {
    vector<int> v;
    for (int i = 0; i < N; i++) {
      v.push_back(1);
    }
    for (int i = 0; i < 8 - N; i++) {
      v.push_back(0);
    }
    shuffle(v.begin(), v.end(), random_device());
    s = "";
    for (int i = 0; i < 8; i++) {
      s += to_string(v[i]);
    }
    cout << s << endl;
    cin >> N;
    if (N == -1) {
      exit(1);
    }
    if (N == 0) {
      return;
    }
  }
}

int main() {
  // ios_base::sync_with_stdio(false);
  // cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    solve();
    // cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
