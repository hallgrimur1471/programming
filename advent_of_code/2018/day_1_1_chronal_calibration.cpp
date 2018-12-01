#include <iostream>
#include <string>

int main() {
  int frequency_change;
  int current_frequency = 0;

  for (std::string line; std::getline(std::cin, line);) {
    frequency_change = stoi(line);
    current_frequency += frequency_change;
  }

  std::cout << "resulting frequency: " << current_frequency << "\n";
  return 0;
}
