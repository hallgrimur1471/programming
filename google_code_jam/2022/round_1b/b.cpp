#include <bits/stdc++.h>

using namespace std;

long long solve(int N, int P, vector<vector<int>> X) {
	vector<long long> T1(N, 0);
	vector<int> pos1(N, 0);
	vector<long long> T2(N, 0);
	vector<int> pos2(N, 0);

	for (int i = N-1; i >= 0; i--) {
		if (i == N-1) {
			int L = *min_element(X[i].begin(), X[i].end());
			int H = *max_element(X[i].begin(), X[i].end());
			long long Dn = abs(H - L);

			T1[i] = Dn;
			pos1[i] = L;

			T2[i] = Dn;
			pos2[i] = H;
			continue;
		}

		int L = *min_element(X[i].begin(), X[i].end());
		int H = *max_element(X[i].begin(), X[i].end());
		int Di = abs(H - L);

		// T1
		long long cand1 = Di + abs(H - pos1[i+1]) + T1[i+1];
		long long cand2 = Di + abs(H - pos2[i+1]) + T2[i+1];
		T1[i] = min(cand1, cand2);
		pos1[i] = L;

		// T2
		cand1 = Di + abs(L - pos1[i+1]) + T1[i+1];
		cand2 = Di + abs(L - pos2[i+1]) + T2[i+1];
		T2[i] = min(cand1, cand2);
		pos2[i] = H;
	}
	return T1[0] + *min_element(X[0].begin(), X[0].end());
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
  	int N;
  	int P;
  	cin >> N;
  	cin >> P;
  	vector<vector<int>> X;
  	for (int i = 0; i < N; i++) {
  		vector<int> v;
  		for (int j = 0; j < P; j++) {
  			int x;
  			cin >> x;
  			v.push_back(x);
  		}
  		X.push_back(v);
  	}
    long long ans = solve(N, P, X);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}