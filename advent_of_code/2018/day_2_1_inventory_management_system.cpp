#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
  std::vector<std::string> boxes_ids;
  for (std::string line; std::getline(std::cin, line);) {
    boxes_ids.push_back(line);
  }

  int num_contains_2 = 0;
  int num_contains_3 = 0;
  for (int i = 0; (unsigned)i < boxes_ids.size(); i++) {
    std::unordered_map<char, int> char_freqs;
    for (int j = 0; (unsigned)j < boxes_ids[i].length(); j++) {
      char c = boxes_ids[i][j];
      if (char_freqs.find(c) == char_freqs.end()) {
        char_freqs[c] = 1;
      } else {
        char_freqs[c] += 1;
      }
    }
    bool contains_2 = false;
    bool contains_3 = false;
    for (const auto &n : char_freqs) {
      if (n.second == 2) {
        contains_2 = true;
      } else if (n.second == 3) {
        contains_3 = true;
      }
    }
    if (contains_2 == true) {
      num_contains_2 += 1;
    }
    if (contains_3 == true) {
      num_contains_3 += 1;
    }
  }
  int checksum = num_contains_2 * num_contains_3;
  std::cout << "Checksum for list of box IDs: " << checksum << "\n";

  return 0;
}
