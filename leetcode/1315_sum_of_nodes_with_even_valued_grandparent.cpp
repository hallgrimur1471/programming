/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  int sumEvenGrandparent(TreeNode* root) {
    bool p_even = false;
    bool gp_even = false;
    return sumEvenGrandparentHelp(root, p_even, gp_even);
  }
private:
  int sumEvenGrandparentHelp(TreeNode* root, bool p, bool gp) {
    if (root == NULL) {
      return 0;
    }
    int s = 0;
    if (gp) {
      s += root->val;
    }
    gp = p;
    p = (root->val % 2 == 0);
    s += sumEvenGrandparentHelp(root->left, p, gp);
    s += sumEvenGrandparentHelp(root->right, p, gp);
    return s;
  }
};
