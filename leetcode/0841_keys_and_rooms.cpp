#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        unordered_set<int> v;
        deque<int> d;
        d.push_back(0);
        while (!d.empty()) {
            int r = d.front();
            d.pop_front();
            v.insert(r);
            
            if (v.size() == rooms.size()) {
                return true;
            }

            for (auto k: rooms[r]) {
                if (v.find(k) != v.end()) {
                    continue;
                }
                d.push_back(k);
            }
        }
        return false;
    }
};

class Solution2 {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int N = rooms.size();
        unordered_set<int> visited;
        return dfs(rooms, 0, N, visited);
    }
    
    bool dfs(vector<vector<int>>& rooms, int c, int N, unordered_set<int>& visited) {
        if (visited.find(c) != visited.end()) {
            return false;
        }

        visited.insert(c);
        
        if (visited.size() == N) {
            return true;
        }
        
        for (int i = 0; i < rooms[c].size(); i++) {
            if (dfs(rooms, rooms[c][i], N, visited)) {
                return true;
            }
        }
        return false;
    }
};


int main() {
	Solution1 sol1;
	Solution2 sol2;

    //vector<vector<int>> rooms {{1},{2},{3},{}};
    vector<vector<int>> rooms {{2,3},{},{2},{1,3,1}};

    cout << "answer: " << sol1.canVisitAllRooms(rooms) << " " << endl;
    cout << "answer: " << sol2.canVisitAllRooms(rooms) << " " << endl;
}

class Solution3 {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int N = rooms.size();
        unordered_set<int> visited;
        return dfs(rooms, 0, N, visited);
    }
    
    bool dfs(vector<vector<int>>& rooms, int c, int N, unordered_set<int>& visited) {
        visited.insert(c);
        
        if (visited.size() == N) {
            return true;
        }
        
        for (int i = 0; i < rooms[c].size(); i++) {
            if (visited.find(rooms[c][i]) != visited.end()) {
                continue;
            }
            if (dfs(rooms, rooms[c][i], N, visited)) {
                return true;
            }
        }
        return false;
    }
};