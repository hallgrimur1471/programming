#include <iostream>
#include <regex>
#include <string>
#include <unordered_map>
#include <vector>

struct Point {
  int x, y;
};
bool operator==(const Point &lp, const Point &rp) {
  return lp.x == rp.x && lp.y == rp.y;
}
namespace std {
template <> struct hash<Point> {
  typedef Point argument_type;
  typedef std::size_t result_type;
  result_type operator()(argument_type const &point) const noexcept {
    result_type const h1(std::hash<int>{}(point.x));
    result_type const h2(std::hash<int>{}(point.y));
    return h1 ^ (h2 << 1);
  }
};
}

int main() {
  std::vector<std::string> claims;
  for (std::string line; std::getline(std::cin, line);) {
    claims.push_back(line);
  }

  std::unordered_map<Point, int> claim_map;
  for (auto claim : claims) {
    std::regex pattern("#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)");
    std::smatch results;
    std::regex_search(claim, results, pattern);
    int x_start = std::stoi(results[1]);
    int y_start = std::stoi(results[2]);
    int width = std::stoi(results[3]);
    int height = std::stoi(results[4]);
    for (int i = x_start; i < x_start + width; i++) {
      for (int j = y_start; j < y_start + height; j++) {
        Point p = {i, j};
        if (claim_map.find(p) == claim_map.end()) {
          claim_map[p] = 1;
        } else {
          claim_map[p] += 1;
        }
      }
    }
  }
  int num_fabrics_with_two_or_more_claims = 0;
  for (auto claim_mapping : claim_map) {
    if (claim_mapping.second >= 2) {
      num_fabrics_with_two_or_more_claims += 1;
    }
  }
  std::cout << "There are " << num_fabrics_with_two_or_more_claims
            << " fabrics with two or more claims.\n";

  return 0;
}
