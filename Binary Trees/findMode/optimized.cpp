
#include <bits/stdc++.h>
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    std::vector<int> findMode(TreeNode* root) {
        inOrder(root);
        return modes;
    }

private:
    std::vector<int> modes;
    TreeNode* prev = nullptr;   
    int currentCount = 0, maxCount = 0;

    void inOrder(TreeNode* node) {
        if (node == nullptr)
            return;

        inOrder(node->left);

        currentCount = (prev != nullptr && node->val == prev->val) ? currentCount + 1 : 1;

        if (currentCount == maxCount) {
            modes.push_back(node->val);
        } else if (currentCount > maxCount) {
            maxCount = currentCount;
            modes = {node->val};
        }

        prev = node;           
        inOrder(node->right);
    }
};