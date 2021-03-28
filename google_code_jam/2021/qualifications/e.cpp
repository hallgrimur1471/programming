#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

int solve(int (&g)[100][10000]) {
  int prob_cheater[100];
  for (int i = 0; i < 100; i++) {
    prob_cheater[i] = 0;
  }

  for (int j = 0; j < 10000; j++) {
    int num_correct = 0;
    for (int i = 0; i < 100; i++) {
      if (g[i][j] == 1) {
        num_correct++;
      }
    }
    for (int i = 0; i < 100; i++) {
      if (g[i][j] == 1) {
        prob_cheater[i] += 100 - num_correct;
      }
    }
  }

  int mx = -1;
  int mx_i = -1;
  for (int i = 0; i < 100; i++) {
    if (prob_cheater[i] > mx) {
      mx = prob_cheater[i];
      mx_i = i;
    }
  }
  return mx_i + 1;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  int P;
  cin >> P;
  for (int t = 1; t <= T; t++) {
    int g[100][10000];
    for (int i = 0; i < 100; i++) {
      string s;
      cin >> s;
      for (int j = 0; j < 10000; j++) {
        g[i][j] = (int)(s[j] - '0');
      }
    }
    int ans = solve(g);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
