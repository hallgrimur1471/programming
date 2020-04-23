#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<vector<string>> findDuplicate(vector<string>& paths) {
    unordered_map<string, vector<string>> m;
    for (auto path: paths) {
      stringstream ss(path);
      string root;
      getline(ss, root, ' ');
      string info;
      while (getline(ss, info, ' ')) {
        string file_name = info.substr(0, info.find('('));
        string contents = info.substr(info.find('(') + 1, info.find(')'));
        m[contents].push_back(root + "/" + file_name);
      }
    }
    vector<vector<string>> ans;
    for (auto key_val: m) {
      if (key_val.second.size() > 1) {
        ans.push_back(key_val.second);
      }
    }
    return ans;
  }
};

class OldSolution {
public:
  vector<vector<string>> findDuplicate(vector<string>& paths) {
    unordered_map<string, vector<string>> m;
    for (auto path: paths) {
      int p = path.find(' ');
      string dir_path = path.substr(0, p);
      vector<string> files;
      int q = path.find(' ', p+1);
      while (p != string::npos) {
        files.push_back(path.substr(p+1, q-p-1));
        p = q;
        if (p != string::npos) {
          q = path.find(' ', p+1);
        }
      }
      for (auto file: files) {
        int r = file.find('(');
        int s = file.find(')');
        string contents = file.substr(r+1, s-r-1);
        string filename = file.substr(0, r);
        string full_path = dir_path + "/" + filename;
        m[contents].push_back(full_path);
      }
    }
    vector<vector<string>> ans;
    for (auto key_val: m) {
      if (key_val.second.size() > 1) {
        vector<string> part;
        for (auto full_path: key_val.second) {
          part.push_back(full_path);
        }
        ans.push_back(part);
      }
    }
    return ans;
  }
};

int main() {
  vector<string> paths;
  paths.push_back("root/a 1.txt(abcd) 2.txt(efgh)");
  paths.push_back("root/c 3.txt(abcd)");
  paths.push_back("root/c/d 4.txt(efgh)");
  paths.push_back("root 4.txt(efgh)");
  Solution solution;
  vector<vector<string>> ans = solution.findDuplicate(paths);
  cout << "[";
  for (auto v: ans) {
    cout << "[";
    for (int i = 0; i < v.size(); i++) {
      cout << '"' << v[i] << '"';
      if (i != v.size() - 1) {
        cout << ", ";
      }
    }
    cout << "]";
  }
  cout << "]" << endl;
  return 0;
}
