#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ipair;

string find_unknown(string built, unordered_set<string>& known, unordered_set<char> (&chars)[10], int L) {
  if (built.length() == L) {
    if (known.find(built) == known.end()) {
      return built;
    }
    else {
      return (string)"-";
    }
  }

  int i = built.length();
  for (char c: chars[i]) {
    string s = find_unknown(built + c, known, chars, L);
    if (s != "-") {
      return s;
    }
  }
  return (string)"-";
}

string solve(int N, int L, vector<string>& words) {
  unordered_set<string> known;
  unordered_set<char> chars[10];
  for (auto word: words) {
    known.insert(word);
    for (int i = 0; i < L; i++) {
      chars[i].insert(word[i]);
    }
  }
  return find_unknown("", known, chars, L);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, L;
    cin >> N >> L;
    vector<string> words;
    for (int i = 0; i < N; i++) {
      string s;
      cin >> s;
      words.push_back(s);
    }
    string ans = solve(N, L, words);
    cout << "Case #" << t << ": " << ans << "\n";
  }
  return 0;
}
