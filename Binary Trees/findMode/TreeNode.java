import java.util.List;

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
    private int currentVal;
    private int currentCount = 0;
    private int maxCount = 0;
    private List<Integer> modes = new ArrayList<>();
    public int[] findMode(TreeNode root) {
        inOrder(root);
        int[] solution = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) {
            solution[i] = modes.get(i);
        }
        return solution;
    }
    private void inOrder(TreeNode node){
        if(node == null) return;

        inOrder(node.left);
        currentCount = (node.val == currentVal) ? currentCount+1 : 1;
        if(currentCount == maxCount){
            modes.add(node.val);
        }else if(currentCount > maxCount){
            maxCount = currentCount;
            modes.clear();
            modes.add(node.val);
        }
        currentVal = node.val;
        inOrder(node.right);
    }

}