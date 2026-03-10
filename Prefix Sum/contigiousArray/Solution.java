import java.util.HashMap;

class Solution {
    public int findMaxLength(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int runningsum = 0;
        int answer = 0;
        map.put(0,-1);

        for (int i = 0; i < nums.length; i++) {
            runningsum += (nums[i] == 1) ? 1 : -1;

            if(map.containsKey(runningsum))answer = Math.max(answer, i - map.get(runningsum));
            else map.put(runningsum, i);
        }
        return answer;
    }
}