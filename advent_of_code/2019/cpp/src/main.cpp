#include <iostream>

#include <advent_of_code_2019/days.hpp>
#include <advent_of_code_2019/utils.hpp>

int main(int argc, char *argv[]) {
  std::ifstream input_file_stream;

  if ((std::string)argv[1] != "-d") {
    std::cout << "Usage: ./advent_of_code -d DAY_NUMBER" << std::endl;
    return 1;
  }

  int day_num = std::atoi(argv[2]);
  switch (day_num) {
  case 1: {
    utils::open_input_file(day_num, input_file_stream);
    solve_day_1(input_file_stream);
    break;
  }
  case 2: {
    solve_day_2();
    break;
  }
  }
  std::cout << "Done" << std::endl;
  return 0;
}
