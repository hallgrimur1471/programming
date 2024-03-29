// Run interactive problem:
// run-when-modified.py . .cpp 'clear; g++ -std=c++14 -pthread -O3 b.cpp &&
// python3 ../../../interactive_runner.py python3 b_testing_tool.py 0 --
// ./a.out'

// Run normal problem:
// svarmi_watch . .cpp "clear; g++ a.cpp -std=c++17 -pthread -O2 && ./a.out <
// a.ex"

// Start of file
#include <bits/stdc++.h>
using namespace std;

// Type less
typedef long long ll;
typedef pair<int, int> ipair;

// inject to std how to hash a pair of ints
namespace std {
template <>
struct hash<pair<int, int>> {
  size_t operator()(pair<int, int> const &p) const noexcept {
    return hash<int>()(p.first) ^ hash<int>()(p.second);
  }
};
}  // namespace std

// Create Mersenne Twister 19937
mt19937 rng(1234);

// Debug printing
#define watch(x) cout << (#x) << " is " << (x) << endl

// Vector to string:
// {1, 2, 3} -> "1 2 3"
template <typename T>
string v2s(vector<T> v) {
  ostringstream ss;
  for (auto it = v.begin(); it != v.end(); it++) {
    ss << *it;
    if (it != prev(v.end())) {
      ss << " ";
    }
  }
  return ss.str();
}

/* Function to check if x is power of 2*/
bool isPowerOfTwo(int x) {
  /* First x in the below expression is
   *     for the case when x is 0 */
  return x && (!(x & (x - 1)));
}

// Number of digits in N =floor(log10(N)) + 1;

//// A quick way to swap a and b
//    a ^= b;
//    b ^= a;
//    a ^= b;

// n = n << 1;   // Multiply n with 2
// n = n >> 1;   // Divide n by 2

// if (num & 1)
//   cout << "ODD";
// else
//   cout << "EVEN";