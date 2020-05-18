class Solution {
public:
  int subarrayBitwiseORs(vector<int> &A) {
    // This solution still receives TLE when submitted,
    // I ended up submitting the same algorithm in Python
    // which succeded without TLE.
    unordered_set<int> ans;
    set<int> ors;
    for (int ai : A) {
      set<int> new_ors;
      new_ors.insert(ai);
      for (int elem : ors)
        new_ors.insert(ai | elem);
      ors = new_ors;
      for (int elem : ors)
        ans.insert(elem);
    }
    return ans.size();
  }
};

class WrongSolution2 {
public:
  int subarrayBitwiseORs(vector<int> &A) {
    unordered_set<int> ors;
    for (int i = 0; i < A.size(); i++) {
      vector<int> elems;
      for (int elem : ors) {
        elems.push_back(elem);
      }
      for (int elem : elems) {
        ors.insert(elem | A[i]);
      }
      ors.insert(A[i]);
    }
    return ors.size();
  }
};

class WrongSolution1 {
public:
  int subarrayBitwiseORs(vector<int> &A) {
    vector<vector<int>> m;
    for (int i = 0; i < A.size(); i++) {
      vector<int> line;
      for (int j = 0; j < A.size(); j++) {
        line.push_back(0);
      }
      m.push_back(line);
    }
    unordered_set<int> results;
    for (int i = 0; i < A.size(); i++) {
      for (int j = i; j < A.size(); j++) {
        int result;
        if (i == j) {
          result = A[j];
        } else {
          result = m[i][j - 1] | A[j];
        }
        m[i][j] = result;
        results.insert(result);
      }
    }
    return results.size();
  }
};
