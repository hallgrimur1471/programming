class Solution {
public:
  bool canCross(vector<int> &stones) {
    int i = stones.size() - 1;
    return canEndAtWithPowerRange(stones, i, 1, stones[i]);
  }

private:
  bool canEndAtWithPowerRange(vector<int> &stones, int i, int r1, int r2) {
    if (i == 0) {
      return (stones[1] == 1 && r1 == 0 && r2 == 2);
    }
    int j = i - 1;
    while ((j >= 0) && (stones[i] - stones[j] <= i) &&
           (stones[i] - stones[j] <= r2)) {
      int power_j_to_i = stones[i] - stones[j];
      if (power_j_to_i < r1) {
        continue;
      }
      if (canEndAtWithPowerRange(stones, j, power_j_to_i - 1,
                                 power_j_to_i + 1)) {
        return true;
      }
      j--;
    }
    return false;
  }
};
