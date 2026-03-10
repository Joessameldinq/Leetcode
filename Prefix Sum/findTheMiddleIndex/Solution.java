class Solution {
    public int findMiddleIndex(int[] nums) {
        int n = nums.length;
        //Build prefix sum array
        int[] prefixSum  = new int[n];
        for(int i = 1 ; i < n;i++){
            prefixSum[i] = prefixSum[i-1] + nums[i-1];
        }

        //Build suffix sum array
        int[] suffixSum = new int[n];
        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + nums[i + 1];
        }

        //Comparison
        for(int i = 0 ;i  < n;i++){
            if(prefixSum[i] == suffixSum[i]){
                return i;
            }
        }
        return -1;

    }
}