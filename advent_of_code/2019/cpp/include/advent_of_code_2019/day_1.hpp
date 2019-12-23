#include <algorithm>
#include <exception>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

void solve_day_1(std::ifstream &input_file_stream);
long solve_part_1(std::vector<int> masses);
long solve_part_2(std::vector<int> masses);
int fuel_for_mass(int module);
int calculate_module_fuel_requirement(int module);
std::vector<int> parse_day_input_file(std::ifstream &input_file_stream);
