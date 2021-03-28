#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

int solve(int X, int Y, string s) {
  int p, q = 0;

  char last = 0;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '?' && last == 0) {
      continue;
    }
    if (s[i] == '?') {
      s[i] = last;
    }
    last = s[i];
  }

  last = 0;
  for (int i = s.size() - 1; i >= 0; i--) {
    if (last == 0) {
      continue;
    }
    if (s[i] == '?') {
      s[i] = last;
    }
    last = s[i];
  }

  int cost = 0;
  for (int i = 0; i < s.size() - 1; i++) {
    if (s[i] == 'C' && s[i + 1] == 'J') {
      cost += X;
    } else if (s[i] == 'J' && s[i + 1] == 'C') {
      cost += Y;
    }
  }
  return cost;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int X, Y;
    cin >> X >> Y;
    string S;
    cin >> S;
    int ans = solve(X, Y, S);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
