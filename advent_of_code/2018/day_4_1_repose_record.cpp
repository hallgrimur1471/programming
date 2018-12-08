#include <algorithm>
#include <iomanip>
#include <iostream>
#include <regex>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

#include <boost/date_time/gregorian/gregorian.hpp>

struct DutyInfo {
  std::string guard;
  std::array<bool, 60> asleep;
};

bool operator==(const std::pair<std::string, std::string> &ls,
                const std::pair<std::string, std::string> &rs) {
  return ls.first == rs.first && ls.second == rs.second;
}
namespace std {
template <> struct hash<std::pair<std::string, std::string>> {
  typedef std::pair<std::string, std::string> argument_type;
  typedef std::size_t result_type;
  result_type operator()(argument_type const &string_pair) const noexcept {
    result_type const h1(std::hash<string>{}(string_pair.first));
    result_type const h2(std::hash<string>{}(string_pair.second));
    return h1 ^ (h2 << 1);
  }
};
}

int main() {
  std::vector<std::string> records;
  for (std::string line; std::getline(std::cin, line);) {
    records.push_back(line);
  }
  boost::gregorian::date start(1518, 2, 28);
  std::cout << start + boost::gregorian::date_duration(1) << std::endl;

  // struct {
  //  bool operator()(std::string a, std::string b) const {
  //    std::regex pattern("\\[(.+) ([0-9]+):([0-9]+)\\] .+");
  //    std::smatch results;

  //    std::regex_search(a, results, pattern);
  //    std::string a_date = results[1];
  //    int a_hour = stoi(results[2]);
  //    int a_minute = stoi(results[3]);

  //    std::regex_search(b, results, pattern);
  //    std::string b_date = results[1];
  //    int b_hour = stoi(results[2]);
  //    int b_minute = stoi(results[3]);

  //    if (a_date < b_date) {
  //      return true;
  //    } else if (a_date > b_date) {
  //      return false;
  //    } else {
  //      if (a_hour == 23 && b_hour != 23) {
  //        return false;
  //      } else if (a_hour != 23 && b_hour == 23) {
  //        return true;
  //      } else if (a_hour == 23 && b_hour == 23) {
  //        return a_minute < b_minute;
  //      } else {
  //        return a_minute < b_minute;
  //      }
  //    }

  //    return a < b;
  //  }
  //} sorting_comparison;
  // std::sort(records.begin(), records.end(), sorting_comparison);

  // for (auto record : records) {
  //  std::cout << record << "\n";
  //}

  // std::unordered_map<std::string, DutyInfo> date_map;
  // for (auto record : records) {
  //  std::regex pattern("\\[(.+) ([0-9]+):([0-9]+)\\] (.+)");
  //  std::smatch results;
  //  std::regex_search(record, results, pattern);
  //  std::string date = results[1];
  //  int hour = std::stoi(results[2]);
  //  int minute = std::stoi(results[3]);
  //  std::string action = results[4];
  //  std::cout << "processing: " << record << "\n";
  //  if (hour == 23) {
  //    std::cout << "looking at date: " << date << "\n";
  //    std::regex date_pattern("([0-9]+-[0-9]+-)([0-9]+)");
  //    std::regex_search(date, results, date_pattern);
  //    std::ostringstream oss;
  //    oss << std::setw(2) << std::setfill('0') << std::stoi(results[2]) + 1;
  //    std::string new_day = oss.str();
  //    date = (std::string)results[1] + new_day;
  //    std::cout << "date is now: " << date << "\n";
  //  }
  //  if (date_map.find(date) == date_map.end()) {
  //    std::regex guard_id_action_pattern("Guard #([0-9]+) begins shift");
  //    int guard_id;
  //    std::cout << "action: " << action << "\n";
  //    if (std::regex_search(action, results, guard_id_action_pattern)) {
  //      guard_id = std::stoi(results[1]);
  //    } else {
  //      std::cerr << "Error: Expected a 'Guard begins shift' action\n";
  //      return 1;
  //    }
  //    DutyInfo duty_info;
  //    duty_info.guard = guard_id;
  //    std::array<bool, 60> asleep;
  //    for (int i = 0; (unsigned)i < asleep.size(); i++) {
  //      asleep[i] = false;
  //    }
  //    duty_info.asleep = asleep;
  //    date_map[date] = duty_info;
  //  }
  //}

  std::cout << "Hello, World!\n";
  return 0;
}
