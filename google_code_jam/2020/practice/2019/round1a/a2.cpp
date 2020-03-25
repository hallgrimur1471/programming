//
// O(N^2) solution
//
#include <bits/stdc++.h>

using namespace std;

#define watch(x) cerr << (#x) << " is " << (x) << endl
//#define watch(x)

typedef long long ll;
typedef pair<int, int> ipair;

// inject to std how to hash a pair of ints
namespace std {
template <> struct hash<ipair> {
  size_t operator()(ipair const &p) const noexcept {
    return hash<int>()(p.first) ^ hash<int>()(p.second);
  }
};
}

mt19937 rng(1234);

pair<string, vector<ipair>> solve(int r, int c) {
  int mn, mx;
  tie(mn, mx) = minmax(r, c);
  if ((mn == 2 && mx <= 4) || (mn == 3 && mx == 3)) {
    vector<ipair> path;
    return make_pair("IMPOSSIBLE", path);
  }

  set<ipair> all_positions;
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      all_positions.insert(make_pair(i, j));
    }
  } // O(N log N)

  set<ipair> possible_jumps;
  vector<ipair> path;
  while (true) {
    set<ipair> visited;
    path.clear();
    for (auto p : all_positions) {
      possible_jumps.insert(p);
    } // O(N log N)

    while (!possible_jumps.empty()) {
      uniform_int_distribution<int> distri(0, possible_jumps.size() - 1);
      int random_jump_index = distri(rng);
      auto it = possible_jumps.begin();
      advance(it, random_jump_index);
      ipair next_jump = *it;

      visited.insert(next_jump); // O(log N)
      path.push_back(next_jump); // O(1)

      possible_jumps.clear();
      set_difference(all_positions.begin(), all_positions.end(),
                     visited.begin(), visited.end(),
                     inserter(possible_jumps, possible_jumps.begin()));
      int y, x;
      tie(y, x) = next_jump;
      for (auto it = possible_jumps.begin(); it != possible_jumps.end(); it++) {
        int i, j;
        tie(i, j) = (*it);
        if (i == y || j == x) {
          it = possible_jumps.erase(it); // O(1)
        } else if (j - i == x - y || j + i == x + y) {
          it = possible_jumps.erase(it); // O(1)
        }
      } // O(N)
    }   // O(N^2)
    if (path.size() == r * c) {
      break;
    }
  }

  if (path.size() == r * c) {
    return make_pair("POSSIBLE", path);
  } else {
    return make_pair("IMPOSSIBLE", path);
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t < T + 1; t++) {
    int R, C;
    cin >> R >> C;
    watch(R);
    watch(C);

    string ans;
    vector<ipair> path;
    tie(ans, path) = solve(R, C);
    cout << "Case #" << t << ": " << ans << "\n";
    if (ans == "POSSIBLE") {
      for (auto jump : path) {
        cout << jump.first + 1 << " " << jump.second + 1 << "\n";
      }
    }
  }
  return 0;
}
