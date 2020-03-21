#include <iostream>
#include <string>
#include <set>
#include <utility>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
  long double d;
  unsigned long long k;
  cin >> d;
  cin >> k;
  long double s = d;
  while (k--) {
    d /= 2;
    s += d;
    if (d < 0.00001) {
      break;
    }
  }
  cout.precision(17);
  cout << s;
  return 0;
}
