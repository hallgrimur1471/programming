#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

void solve() {
    int liked_flavors[205];
    for (int i = 0; i < 205; i++) {
        liked_flavors[i] = 0;
    }

    unordered_set<int> sold;
    int N;
    cin >> N;
    for (int n = 0; n < N; n++) {
        int D;
        cin >> D;

        if (D == -1) {
            exit(1);
        }

        unordered_set<int> requested_flavors;
        for (int d = 0; d < D; d++) {
            int flavor;
            cin >> flavor;
            requested_flavors.insert(flavor);
        }

        for (int flavor: requested_flavors) {
            liked_flavors[flavor]++;
        }

        if (requested_flavors.empty()) {
            cout << "-1" << endl;
        }
        else {
            int chosen_flavor = (*requested_flavors.begin());
            for (auto flavor: requested_flavors) {
                if ((sold.find(chosen_flavor) != sold.end()) || ( (liked_flavors[flavor] < liked_flavors[chosen_flavor]) && (sold.find(flavor) == sold.end()) )) {
                    chosen_flavor = flavor;
                }
            }

            if (sold.find(chosen_flavor) != sold.end()) {
                cout << "-1" << endl;
            }
            else {
                cout << to_string(chosen_flavor) << endl;
                sold.insert(chosen_flavor);
            }
        }
    }

}

int main() {
  //ios_base::sync_with_stdio(false);
  //cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    solve();
    // cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
