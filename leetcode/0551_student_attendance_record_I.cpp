class Solution {
  public:
    bool checkRecord(string s) {
      int a_seen = 0;
      int l_streak = 0;
      for (auto c: s) {
        if (c == 'A') {
          a_seen += 1;
        }
        if (c == 'L') {
          l_streak += 1;
        }
        else {
          l_streak = 0;
        }
        if (a_seen > 1 || l_streak > 2) {
          return false;
        }
      }
      return true;
    }
};
