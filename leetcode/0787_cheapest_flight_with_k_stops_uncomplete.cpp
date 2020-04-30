#include <bits/stdc++.h>

using namespace std;

int MAX_INT = 2147483647;

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
  int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst,
                        int K) {
    unordered_map<pair<int, int>, int> cost_map;
    unordered_map<int, vector<int>> inbors_map;
    for (auto flight : flights) {
      cost_map[make_pair(flight[0], flight[1])] = flight[2];
      inbors_map[flight[1]].push_back(flight[0]);
    }
    unordered_set<int> visited;
    unordered_map<int, pair<int, bool>> memory;
    int cheapest_price;
    bool is_valid;
    tie(cheapest_price, is_valid) = findCheapestPriceHelp(
        src, dst, K, inbors_map, cost_map, visited, memory);
    if (is_valid) {
      return cheapest_price;
    } else {
      return -1;
    }
  }

private:
  pair<int, bool>
  findCheapestPriceHelp(int src, int dst, int k,
                        const unordered_map<int, vector<int>> &inbors_map,
                        const unordered_map<pair<int, int>, int> &cost_map,
                        unordered_set<int> visited,
                        unordered_map<int, pair<int, bool>> memory) {
    visited.insert(dst);
    if (src == dst) {
      return make_pair(0, true);
    }
    if (k == -1 || inbors_map.find(dst) == inbors_map.end()) {
      return make_pair(NULL, false);
    }
    bool found_valid = false;
    int cheapest_to_dst = MAX_INT;
    for (auto u : inbors_map.at(dst)) {
      if (visited.find(u) != visited.end()) {
        continue;
      }
      int cheapest_to_u;
      bool is_valid;
      if (memory.find(u) != memory.end()) {
        tie(cheapest_to_u, is_valid) = memory.at(u);
      } else {
        tie(cheapest_to_u, is_valid) = findCheapestPriceHelp(
            src, u, k - 1, inbors_map, cost_map, visited, memory);
      }
      if (is_valid) {
        found_valid = true;
        memory[u] = make_pair(cheapest_to_u, is_valid);
        cheapest_to_dst = min(cheapest_to_dst,
                              cheapest_to_u + cost_map.at(make_pair(u, dst)));
      }
    }
    return make_pair(cheapest_to_dst, found_valid);
  }
};
