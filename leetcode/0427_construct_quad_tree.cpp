/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }

    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node*
_bottomLeft, Node* _bottomRight) { val = _val; isLeaf = _isLeaf; topLeft =
_topLeft; topRight = _topRight; bottomLeft = _bottomLeft; bottomRight =
_bottomRight;
    }
};
*/

class Solution {
public:
  Node *construct(vector<vector<int>> &grid) {
    int x_min, x_max, y_min, y_max;
    x_min = y_min = 0;
    x_max = y_max = grid.size();
    return construct_help(grid, x_min, x_max, y_min, y_max)
  }

private:
  Node *construct_help(vector<vector<int>> &grid, int x_min, int x_max,
                       int y_min, int y_max) {
    unordered_set<int> vals;
    bool is_uniform = true;
    for (int i = y_min; i < y_max; i++) {
      for (int j = x_min; j < x_max; j++) {
        vals.insert(grid[i][j]);
        if (vals.size() > 1) {
          is_uniform = false;
          break;
        }
      }
      if (!is_uniform) {
        break;
      }
    }
    if (is_uniform) {
      return Node((*vals.begin()), true);
    }
  }
};
