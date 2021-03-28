#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

int solve(int X, int Y, string s) {
  int p, q = 0;

  if (s[0] == '?') {
    while (s[q] == '?' && q < s.size()) q++;
    char choice = (q == s.size()) ? 'C' : s[q];
    for (int i = p; i < q; i++) s[i] = choice;
    p = q;
  }

  while (p < s.size()) {
    while (p + 1 < s.size() && s[p + 1] != '?') p++;
    if (p + 1 == s.size()) {
      break;
    }
    q = p + 1;
    while (q < s.size() && s[q] == '?') q++;
    char choice;
    if (q == s.size()) {
      choice = s[p];
    } else {
      if (s[p] == s[q]) {
        choice = s[p];
      } else {
        choice = s[p];  // lol?
      }
    }
    for (int i = p; i < q; i++) s[i] = choice;
  }
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
