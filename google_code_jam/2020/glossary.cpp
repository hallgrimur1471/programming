// Run interactive problem:
// run-when-modified.py . .cpp 'clear; g++ -std=c++14 -pthread -O3 b.cpp &&
// python3 ../../../interactive_runner.py python3 b_testing_tool.py 0 --
// ./a.out'

// Run normal problem:
// run-when-modified.py . .cpp 'clear; g++ -std=c++14 -pthread -O3 b.cpp && cat
// b.ex | time ./a.out'

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
