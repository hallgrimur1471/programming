class Solution {
public:
  bool canCross(vector<int> &stones) {
    int i = stones.size() - 1;
    return canEndAtWithPowerRange(stones, i, 1, stones[i]);
  }

  // [0,1,3,4,5,7,9,10,12]
  // [0,1,2,3,4,8,9,11]
private:
  bool canEndAtWithPowerRange(vector<int> &stones, int i, int r1, int r2) {
    if (i == 0) {
      return (stones[1] == 1 && r1 == 0 && r2 == 2);
    }
    int j = i;
    while (true) {
      j--;
      if (j < 0) {
        break;
      }
      if (stones[i] - stones[j] > i) {
        break;
      }
      if (stones[i] - stones[j] > r2) {
        break;
      }
      if (stones[i] - stones[j] < r1) {
        continue;
      }
      int power_j_to_i = stones[i] - stones[j];
      if (canEndAtWithPowerRange(stones, j, power_j_to_i - 1,
                                 power_j_to_i + 1)) {
        cout << i << " ";
        return true;
      }
    }
    return false;
  }
};
