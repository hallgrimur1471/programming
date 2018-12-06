#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> input_data;
  for (std::string line; std::getline(std::cin, line);) {
    input_data.push_back(line);
  }

  std::cout << "Hello, World!\n";
  return 0;
}
