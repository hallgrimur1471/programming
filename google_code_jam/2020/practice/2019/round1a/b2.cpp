#include <bits/stdc++.h>

using namespace std;

#define watch(x) cerr << (#x) << " is " << (x) << endl

#define OPI(v)                                                                 \
  for (auto e : v) {                                                           \
    cout << e << " ";                                                          \
  }                                                                            \
  cout << endl;

#define EPI(v)                                                                 \
  for (auto e : v) {                                                           \
    cerr << e << " ";                                                          \
  }                                                                            \
  cerr << endl;

// Begin: divisors are all pairwise coprime, and sorted in descending order
template <class T>
int use_chineese_remainder_theorem(T divisors_begin, T divisors_end,
                                   T remainders_begin, T remainders_end) {
  auto dc_it = divisors_begin;
  auto rc_it = remainders_begin;
  int x = (*rc_it);
  while (true) {
    while ((dc_it != divisors_end) && ((x % (*dc_it)) == (*rc_it))) {
      dc_it++;
      rc_it++;
    }
    if (dc_it == divisors_end) {
      break;
    } else {
      dc_it = divisors_begin;
      rc_it = remainders_begin;
      x += (*dc_it);
    }
  }
  return x;
}

void solve(int T, int N, int M) {
  array<int, 6> bc = {18, 17, 13, 11, 7, 5};
  array<int, 6> rs;

  for (int n = 0; n < 6; n++) {
    array<int, 18> mills;
    mills.fill(bc[n]);
    OPI(mills);
    array<int, 18> brs;
    for (int i = 0; i < 18; i++) {
      int br;
      cin >> br;
      if (br == -1) {
        exit(1);
      } else {
        brs[i] = br;
      }
    }
    int r = accumulate(brs.begin(), brs.end(), 0) % bc[n];
    rs[n] = r;
  }

  int G = use_chineese_remainder_theorem(bc.begin(), bc.end(), rs.begin(),
                                         rs.end());
  cout << G << endl;
  int ans;
  cin >> ans;
  if (ans == -1) {
    exit(1);
  }
}

int main() {
  int T, N, M;
  cin >> T >> N >> M;
  watch(M);
  for (int t = 1; t <= T; t++) {
    solve(T, N, M);
  }
  return 0;
}
