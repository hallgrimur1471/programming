#include <bits/stdc++.h>

class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
    	unordered_set<int> seen;
    	for (int a: A) {
    		if (seen.find(a) != seen.end()) {
    			return a;
    		}
    		seen.insert(a);
    	}
    	return NULL;
    }
};