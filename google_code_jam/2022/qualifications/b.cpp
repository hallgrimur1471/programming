#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

int solve(int N, vector<int> S) {
    sort(S.begin(), S.end());
    vector<int> m(S.size() + 1, 0);

    for (int i = 1; i < m.size(); i++) {
        if (S[i - 1] > m[i - 1]) {
            m[i] = m[i - 1] + 1;
        } else {
            m[i] = m[i - 1];
        }
    }

    return m.back();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<int> S;
        for (int i = 0; i < N; i++) {
            int s;
            cin >> s;
            S.push_back(s);
        }
        int ans = solve(N, S);
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}