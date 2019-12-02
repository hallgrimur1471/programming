// Problem:
//   Calculate the sum of two integers a and b,
//   but you are not allowed to use the operator + and -.

class Solution {
public:
    int getSum(int a, int b) {
        unsigned int x, y, z;
        
        x = a;
        y = b;
        while (x != 0) {
            z = (x & y) << 1;
            y = x ^ y;
            x = z;
        }
        
        return (int)y;
    }
};