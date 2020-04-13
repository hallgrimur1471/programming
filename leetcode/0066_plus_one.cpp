// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
// 
// The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
// 
// You may assume the integer does not contain any leading zero, except the number 0 itself.

// [9, 9, 9] -> [1, 0, 0, 0]
// [8, 9, 9] -> [9, 0, 0]

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
    	int i = digits.size() - 1;
    	int carry = 1;
    	while(carry && i >= 0) {
    		digits[i]++;
    		digits[i] %= 10;
    		if (digits[i] == 0) {
    			carry = 1;
    		}
    		else {
    			carry = 0;
    		}
    		if (carry && i == 0) {
    			digits[i] = 1;
    			digits.push_back(0);
    			break;
    		}
    		i--;
    	}
    	return digits;
    }
};

int main() {
	Solution solution;
	vector<int> ds1 = {9, 9, 9};
	vector<int> ds2 = solution.plusOne(ds1);
	for (auto d: ds1) {
		cout << d << " ";
	}
	cout << "\n";
	for (auto d: ds2) {
		cout << d << " ";
	}
	cout << "\n";
}