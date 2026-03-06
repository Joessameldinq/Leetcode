import java.util.*;
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private Integer previous = null;
    private int min_diff = Integer.MAX_VALUE;
    public int getMinimumDifference(TreeNode root) {
        inOrder(root);
        return min_diff;
    }
    private void inOrder(TreeNode node){
        if(node == null)return;
        inOrder(node.left);
        if(previous != null)
            min_diff = Math.min(min_diff,Math.abs(node.val-previous));
        previous = node.val;
        inOrder(node.right);
    }
}