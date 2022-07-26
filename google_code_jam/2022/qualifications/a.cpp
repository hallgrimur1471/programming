#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

void solve(int R, int C) {
    string s = "..+";
    for (int i = 0; i < C - 1; i++) {
        s.append("-+");
    }
    cout << s << endl;

    for (int i = 0; i < R; i++) {
        if (i == 0) {
            s = ".";
        } else {
            s = "|";
        }
        for (int j = 0; j < C; j++) {
            s.append(".|");
        }
        cout << s << endl;
        s = "+";
        for (int j = 0; j < C; j++) {
            s.append("-+");
        }
        cout << s << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int R, C;
        cin >> R >> C;
        cout << "Case #" << t << ":" << endl;
        solve(R, C);
    }
    return 0;
}
