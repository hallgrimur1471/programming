//
// O(N^2) solution
//
#include <bits/stdc++.h>

#define watch(x) cerr << (#x) << " is " << (x) << endl

typedef long long ll;

using namespace std;

// inject to std how to hash a pair of ints
namespace std {
template <> struct hash<pair<int, int>> {
  size_t operator()(pair<int, int> const &p) const noexcept {
    return hash<int>()(p.first) ^ hash<int>()(p.second);
  }
};
}

pair<string, vector<pair<int, int>>> solve(int r, int c) {
  int mn, mx;
  tie(mn, mx) = minmax(r, c);
  if ((mn == 2 && mx <= 4) || (mn == 3 && mx == 3)) {
    vector<pair<int, int>> path;
    return make_pair("IMPOSSIBLE", path);
  }

  unordered_set<pair<int, int>> all_positions;
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      all_positions.insert(make_pair(i, j));
    }
  } // O(N)

  unordered_set<pair<int, int>> possible_jumps;
  mt19937 rng(1234);
  vector<pair<int, int>> path;
  while (true) {
    cerr << "TRY" << endl;
    unordered_set<pair<int, int>> visited;
    path.clear();
    for (auto p : all_positions) {
      possible_jumps.insert(p);
    } // O(N)

    while (!possible_jumps.empty()) {
      uniform_int_distribution<int> distri(0, possible_jumps.size() - 1);
      int random_jump_index = distri(rng);
      // watch(random_jump_index);
      auto next_jump_it = possible_jumps.begin();
      while (random_jump_index--) {
        next_jump_it++;
      }
      pair<int, int> next_jump = (*next_jump_it);

      visited.insert(next_jump);
      path.push_back(next_jump);

      int i = next_jump.first;
      int j = next_jump.second;
      possible_jumps.clear();
      for (auto p : all_positions) {
        if (p.first == i || p.second == j) {
          continue;
        } else if (p.second - p.first == j - i || p.second + p.first == j + i) {
          continue;
        } else if (visited.find(p) != visited.end()) {
          continue;
        } else {
          possible_jumps.insert(p);
        }
      } // O(N)
    }   // O(N^2)
    if (path.size() == r * c) {
      break;
    }
    watch(tries_left);
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
    vector<pair<int, int>> path;
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
