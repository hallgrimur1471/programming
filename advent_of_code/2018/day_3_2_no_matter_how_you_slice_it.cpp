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

struct ClaimInfo {
  int id;
  int x_start;
  int y_start;
  int width;
  int height;
};

ClaimInfo get_claim_info(std::string claim) {
  std::regex pattern("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)");
  std::smatch results;
  std::regex_search(claim, results, pattern);
  ClaimInfo claim_info;
  claim_info.id = std::stoi(results[1]);
  claim_info.x_start = std::stoi(results[2]);
  claim_info.y_start = std::stoi(results[3]);
  claim_info.width = std::stoi(results[4]);
  claim_info.height = std::stoi(results[5]);
  return claim_info;
}

int main() {
  std::vector<std::string> claims;
  for (std::string line; std::getline(std::cin, line);) {
    claims.push_back(line);
  }

  std::unordered_map<Point, int> claim_map;
  for (auto claim : claims) {
    auto ci = get_claim_info(claim);
    for (int i = ci.x_start; i < ci.x_start + ci.width; i++) {
      for (int j = ci.y_start; j < ci.y_start + ci.height; j++) {
        Point p = {i, j};
        if (claim_map.find(p) == claim_map.end()) {
          claim_map[p] = 1;
        } else {
          claim_map[p] += 1;
        }
      }
    }
  }
  for (auto claim : claims) {
    bool overlaps = false;
    auto ci = get_claim_info(claim);
    for (int i = ci.x_start; i < ci.x_start + ci.width; i++) {
      for (int j = ci.y_start; j < ci.y_start + ci.height; j++) {
        if (claim_map[{i, j}] != 1) {
          overlaps = true;
          goto overlap_determined;
        }
      }
    }
  overlap_determined:
    if (overlaps == false) {
      std::cout << "claim " << ci.id << " does not overlap.\n";
      return 0;
    }
  }

  return 1;
}
