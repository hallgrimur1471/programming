#include <advent_of_code_2019/day_1.hpp>
#include <advent_of_code_2019/utils.hpp>

void solve_day_1(std::ifstream &input_file_stream) {
  std::vector<int> masses;

  masses = parse_day_input_file(input_file_stream);
}

std::vector<int> parse_day_input_file(std::ifstream &input_file_stream) {
  if (!input_file_stream.is_open()) {
    throw std::runtime_error("Input file could not be read");
  }

  std::vector<int> masses;
  std::string line;
  while (std::getline(input_file_stream, line)) {
    int module_mass = std::stoi(line);
    masses.push_back(module_mass);
  }

  return masses;
}
