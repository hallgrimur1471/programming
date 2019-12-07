#include <iostream>

#include <advent_of_code_2019/days.hpp>

int main(int argc, char *argv[]) {
  if ((std::string)argv[1] != "-d") {
    std::cout << "Usage: ./advent_of_code -d DAY_NUMBER" << std::endl;
    return 1;
  }

  int day_num = std::atoi(argv[2]);
  switch (day_num) {
  case 1:
    solve_day_1();
    break;
  case 2:
    solve_day_2();
    break;
  }
  return 0;
}
