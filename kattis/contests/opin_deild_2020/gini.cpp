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

//int main() {
//  int n;
//  cin >> n;
//  vector<int> y;
//  for (int i = 0; i < n; i++) {
//    int x;
//    cin >> x;
//    y.push_back(x);
//  }
//  sort(y.begin(), y.end());
//  long long nom = 0;
//  long long den = 0;
//  for (int i = 1; i < n+1; i++) {
//    nom += i*y[i-1];
//    den += y[i-1];
//  }
//  nom *= 2;
//  den *= n;
//  long double fraction = (long double)nom / den;
//  long double ans = fraction - (((long double)n + 1) / (n));
//  cout.precision(17);
//  cout << ans << endl;
//  return 0;
//}
//
int main() {
  int n;
  cin >> n;
  vector<int> y;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    y.push_back(x);
  }
  sort(y.begin(), y.end());
  long long nom = 0;
  long long den = 0;
  for (int i = 1; i < n+1; i++) {
    nom += (n + 1  - i) * y[i-1];
    den += y[i-1];
  }
  long double fraction = (long double)nom / den;
  long double ans = ((long double)1.0 / (n - 1)) * (n + 1 - (2*fraction));
  cout.precision(17);
  cout << ans << endl;
  return 0;
}
