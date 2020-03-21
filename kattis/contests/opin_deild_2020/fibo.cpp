#include <iostream>
#include <string>
#include <set>
#include <utility>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <cmath>

using namespace std;

//long fib_calc(int n)
//{
//    long a = 0;
//    long b = 1;
//    long modulo = 1000000000 + 7;
//    while (n-- > 1) {
//        long t = a;
//        a = b;
//        b += t;
//        b %= modulo;
//    }
//    return b;
//}

//long fib_calc(int n) { 
//  long modulo = 1000000000 + 7;
//  long double five = 5.0;
//  long double s = sqrt(five);
//  long double phi = (1 + s) / 2; 
//  long double x = powl(phi, n);
//  long y = llround(x);
//  long fibo = llround(y / sqrt(5)) % modulo; 
//  return fibo;
//} 

long f(int n, unordered_map<int, long>& m) {
  if (n < 2) {
    return n;
  }

  if (m.count(n) != 0) {
    return m[n];
  }

  long modulo = 1000000000 + 7;

  long k = (n & 1)? (n+1)/2 : n/2; 
  long fibo = (n & 1)? (f(k, m)*f(k, m) + f(k-1, m)*f(k-1, m)) 
         : (2*f(k-1, m) + f(k, m))*f(k, m); 
  fibo %= modulo;

  if (m.size() * 4 < 900) {
    m[n] = fibo;
  }

  return fibo;
}


int main() {
  int n, m;
  cin >> n;
  cin >> m;
  vector<int> v;
  v.push_back(0);
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    v.push_back(x);
  }
  unordered_map<int, long> cache;
  for (int t = 0; t < m; t++) {
    int op, l, r;
    cin >> op;
    cin >> l;
    cin >> r;
    if (op == 1) {
      int d;
      cin >> d;
      for (int i = l; i <= r; i++) {
        v[i] += d;
      }
    }
    else if (op == 2) {
      long sum = 0;
      long modulo = 1000000000 + 7;
      for (int i = l; i <= r; i++) {
        sum += f(v[i], cache);
        //sum += fib(v[i]);
        sum %= modulo;
      }
      cout << sum << endl;
    }
  }
  return 0;
}
