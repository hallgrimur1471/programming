// inject to std how to hash a pair of ints
namespace std {
template <> struct hash<pair<int, int>> {
  size_t operator()(pair<int, int> const &p) const noexcept {
    return hash<int>()(p.first) ^ hash<int>()(p.second);
  }
};
} // namespace std

class Solution {
public:
  int maxAreaOfIsland(vector<vector<int>> &grid) {
    if (grid.size() == 0) {
      return 0;
    }
    unordered_set<pair<int, int>> known_islands;
    int max_area = 0;
    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid[0].size(); j++) {
        if (grid[i][j] == 0 ||
            known_islands.find(make_pair(i, j)) != known_islands.end()) {
          continue;
        }
        unordered_set<pair<int, int>> island;
        vector<pair<int, int>> to_expand;
        to_expand.push_back(make_pair(i, j));
        while (!to_expand.empty()) {
          int y, x;
          tie(y, x) = to_expand.back();
          to_expand.pop_back();
          island.insert(make_pair(y, x));
          for (int dy = -1; dy < 2; dy++) {
            for (int dx = -1; dx < 2; dx++) {
              if (dy == 0 && dx == 0) {
                continue;
              }
              if (abs(dy) + abs(dx) == 2) {
                continue;
              }
              if (y + dy < 0 || y + dy >= grid.size()) {
                continue;
              }
              if (x + dx < 0 || x + dx >= grid[0].size()) {
                continue;
              }
              if (grid[y + dy][x + dx] == 0) {
                continue;
              }
              if (island.find(make_pair(y + dy, x + dx)) != island.end()) {
                continue;
              }
              to_expand.push_back(make_pair(y + dy, x + dx));
            }
          }
        }
        max_area = max(max_area, (int)island.size());
        for (auto p : island) {
          known_islands.insert(p);
        }
        island.clear();
      }
    }
    return max_area;
  }
};
