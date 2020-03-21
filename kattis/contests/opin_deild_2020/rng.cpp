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

int f(int x, int a, int b, int m) {
  long long q = (a*x + b) % m;
  return (int)q;
}

int main() {
  int a, b, x, m;
  long long n;
  cin >> a;
  cin >> b;
  cin >> x;
  cin >> n;
  cin >> m;
  int rng  = x;
  unordered_set<int> known;
  long long i = 0;
  bool looped = false;
  while (i < n) {
    if (!looped && known.find(rng) != known.end()) {
      //cout << "loop at i: " << i << endl;
      //cout << "i jumping from " << i << endl;
      i += (i * ((n - i) / i));
      //cout << "to " << i << endl;
      looped = true;
    }

    known.insert(rng);

    rng = f(rng, a, b, m);

    i += 1;

  }
  cout << rng << endl;
  return 0;
}
