#include <climits>
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
    int getMinimumDifference(TreeNode* root) {
        inOrder(root);
        return minDiff;
    }
private:
    TreeNode* previous = nullptr;
    int minDiff = INT_MAX;
    void inOrder(TreeNode* node){
        if(!node)return;
        inOrder(node->left);
        
        if(previous)
            minDiff = std::min(minDiff,std::abs(previous->val-node->val));
        previous = node;
        inOrder(node->right);
    }
};