#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
  std::vector<std::string> boxes_ids;
  for (std::string line; std::getline(std::cin, line);) {
    boxes_ids.push_back(line);
  }

  for (int i = 0; (unsigned)i < boxes_ids.size(); i++) {
    for (int j = i; (unsigned)j < boxes_ids.size(); j++) {
      int num_differing_chars = 0;
      for (int k = 0; (unsigned)k < boxes_ids[i].length(); k++) {
        if (boxes_ids[i][k] != boxes_ids[j][k]) {
          num_differing_chars += 1;
        }
      }
      if (num_differing_chars == 1) {
        std::string common_chars = "";
        for (int k = 0; (unsigned)k < boxes_ids[i].length(); k++) {
          if (boxes_ids[i][k] == boxes_ids[j][k]) {
            common_chars += boxes_ids[i][k];
          }
        }
        std::cout << "These box IDs differ only by one character:\n";
        std::cout << boxes_ids[i] << "\n";
        std::cout << boxes_ids[j] << "\n";
        std::cout << "Their common characters are: " << common_chars << "\n";
        return 0;
      }
    }
  }

  return 1;
}
