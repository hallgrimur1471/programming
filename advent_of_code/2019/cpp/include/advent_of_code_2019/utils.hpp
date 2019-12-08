#include <fstream>
#include <iostream>
#include <string>

namespace utils {

void open_input_file(int day_number, std::ifstream &input_file_stream);
std::string get_input_file_path(int day_number);
}
