#include <bits/stdc++.h>

using namespace std;

int solve(int N, deque<int> D) {
	int num_payed = 0;
	int mx_served = 0;
	while (!D.empty()) {
		if (D.front() < D.back()) {
			if (D.front() >= mx_served) {
				mx_served = D.front();
				num_payed++;
			}
			D.pop_front();
		} else {
			if (D.back() >= mx_served) {
				mx_served = D.back();
				num_payed++;
			}
			D.pop_back();
		}
	}
	return num_payed;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
  	int N;
  	cin >> N;
  	deque<int> D;
  	for (int i = 0; i < N; i++) {
  		int x;
  		cin >> x;
  		D.push_back(x);
  	}
    int ans = solve(N, D);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
