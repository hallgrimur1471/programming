#include <advent_of_code_2019/day_1.hpp>
#include <advent_of_code_2019/utils.hpp>

void solve_day_1(std::ifstream &input_file_stream) {
  std::vector<int> masses;

  masses = parse_day_input_file(input_file_stream);

  long answer_1 = solve_part_1(masses);
  std::cout << "The sum of the fuel requirements is " << answer_1 << std::endl;

  long answer_2 = solve_part_2(masses);
  std::cout << "The sum of the fuel requirements is actually " << answer_2
            << std::endl;
}

long solve_part_1(std::vector<int> masses) {
  std::vector<int> fuel_requirements(masses.size(), 0);
  std::transform(masses.begin(), masses.end(), fuel_requirements.begin(),
                 fuel_for_mass);
  return std::accumulate(fuel_requirements.begin(), fuel_requirements.end(), 0);
}

int fuel_for_mass(int module) {
  int fuel_requirement = (module / 3) - 2;
  return fuel_requirement;
}

long solve_part_2(std::vector<int> masses) {
  long fuel_requirements = 0;
  for (auto module : masses) {
    int fuel_requirement = calculate_module_fuel_requirement(module);
    fuel_requirements += fuel_requirement;
  }
  return fuel_requirements;
}

int calculate_module_fuel_requirement(int module) {
  int fuel_requirement = fuel_for_mass(module);
  int total_required_fuel = fuel_requirement;

  while (fuel_requirement > 0) {
    fuel_requirement = fuel_for_mass(fuel_requirement);
    fuel_requirement = std::max(0, fuel_requirement);
    total_required_fuel += fuel_requirement;
  }

  return total_required_fuel;
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
