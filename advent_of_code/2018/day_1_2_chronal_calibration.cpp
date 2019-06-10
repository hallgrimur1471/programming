#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

int main() {

  std::vector<int> list_of_frequency_changes;
  for (std::string line; std::getline(std::cin, line);) {
    list_of_frequency_changes.push_back(stoi(line));
  }

  int i = 0;
  int current_frequency = 0;
  std::unordered_set<int> frequencies_experienced;
  while (frequencies_experienced.find(current_frequency) ==
         frequencies_experienced.end()) {
    frequencies_experienced.insert(current_frequency);
    current_frequency +=
        list_of_frequency_changes[i++ % list_of_frequency_changes.size()];
  }

  std::cout << "first frequency we reached twice: " << current_frequency
            << "\n";
  return 0;
}
