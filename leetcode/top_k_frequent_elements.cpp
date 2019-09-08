// Problem:
//   Given a non-empty array of integers, return the k most frequent elements.
//   Algorithm's time complexity must be better than O(n*log(n))
//
// Strategy:
//   Collect frequencies to hashmap [O(n)].
//   "Reverse" the hashmap [O(n)].
//   Create priority queue [O(n)].
//   pop k elems from the queue [O(k * log("num unique elements")].
//
// Time complexity:
//   O(n + k*log("num unique elements"))
//   <= O(n + k*log(n))

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> num_to_freq;
        std::unordered_multimap<int, int> freq_to_num;
        std::unordered_set<int> freqs_set;
        std::vector<int> freqs_vector;
        std::vector<int> top_k_frequent_elems;
        
        for (auto& num : nums) {
            if (num_to_freq.count(num) == 0) {
                num_to_freq[num] = 0;
            }
            else {
                num_to_freq[num]++;
            }
        }
        
        for (auto& elem : num_to_freq) {
            freq_to_num.insert({elem.second, elem.first});
        }
        
        for (auto& elem : freq_to_num) {
            freqs_set.insert(elem.first);
        }
        freqs_vector.insert(freqs_vector.end(), freqs_set.begin(), freqs_set.end());
        
        std::priority_queue<int> top_freqs(std::less<int>(), freqs_vector); // heapify is O(N)
        
        while (k > 0) {
            int freq = top_freqs.top();
            top_freqs.pop();
            
            auto equal_range = freq_to_num.equal_range(freq);
            auto it = equal_range.first;
            while (k > 0 && it != equal_range.second) {
                int num = it->second;
                top_k_frequent_elems.push_back(num);
                
                it++;
                k--;
            }
        }
        
        return top_k_frequent_elems;
    }
};