#include <advent_of_code_2019/utils.hpp>

namespace utils {

void open_input_file(int day_number, std::ifstream &input_file_stream) {
  std::string input_file_path = get_input_file_path(day_number);
  input_file_stream.open(input_file_path.c_str());
}

std::string get_input_file_path(int day_number) {
  std::string input_file_path;

  input_file_path = "inputs/day_" + std::to_string(day_number) + ".txt";
  return input_file_path;
};

} // end utils namespace
