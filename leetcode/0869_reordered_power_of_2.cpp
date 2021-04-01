#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool reorderedPowerOf2(int N) {
        int num_digits = to_string(N).length();
        vector<int> cands;
        
        for (int i = 0; ; i++) {
            int n = exp2(i);
            if (to_string(n).length() == num_digits) {
                cands.push_back(n);
            }
            else if (to_string(n).length() > num_digits) {
                break;
            }
        }

        string N_sorted = to_string(N);
        sort(N_sorted.begin(), N_sorted.end());

        for (int c: cands) {
            string s = to_string(c);
            sort(s.begin(), s.end());

            if (s == N_sorted) {
                return true;
            }
        }
        return false;
    }
};

int main() {
	Solution solution;
    cout << solution.reorderedPowerOf2(45);
}