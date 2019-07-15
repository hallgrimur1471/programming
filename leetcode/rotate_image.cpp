#include <iostream>

struct Position {
    int i;
    int j;
};

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n / 2; i++) {
            for (int j=i; j < n - 1 - i; j++) {
                Position p = {i, j};
                int rotations = 0;
                int v = matrix[p.i][p.j];
                while (rotations < 4) {
                    Position rp = rotate_clockwise(p, n);
                    int tmp = matrix[rp.i][rp.j];
                    matrix[rp.i][rp.j] = v;
                    
                    p = rp;
                    v = tmp;
                    rotations++;
                }
            }
        }
    }
    
    Position rotate_clockwise(Position p, int n) {
        int new_j = n - p.i - 1;
        int new_i = p.j;
        
        Position rotated_position = {new_i, new_j};
        return rotated_position;
    }
};