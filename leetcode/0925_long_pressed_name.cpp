#include <bits/stdc++.h>

using namespace std;

class Solution {
   public:
    bool isLongPressedName(string name, string typed) {
        int i = 0;
        int j = 0;
        while (i < name.size()) {
            if (j > typed.size()) {
                return false;
            }

            if (name[i] == typed[j]) {
                i++;
                j++;
            } else if (name[i] != typed[j] && i > 0 &&
                       typed[j] == name[i - 1]) {
                j++;
            } else {
                return false;
            }
        }

        while (j < typed.size()) {
            if (typed[j] != name[i - 1]) {
                return false;
            }
            j++;
        }
        return true;
    }
};

int main() {
    Solution sol;
    string name = "alex";
    string typed = "aalex";

    cout << "answer: " << sol.isLongPressedName("alex", "aalex") << " " << endl;
    cout << "answer: " << sol.isLongPressedName("saeed", "ssaaedd") << " "
         << endl;
    cout << "answer: " << sol.isLongPressedName("alex", "aalexa") << " "
         << endl;
}
