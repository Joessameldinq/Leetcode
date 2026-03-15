import java.util.Stack;

public class MontonicStackTemplate {
    public static int[] monotonicStackTemplate(int[] nums){
        int n = nums.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0 ; i  < n ;i++){
            while(!stack.isEmpty() && violatesMonotonicProperty(nums[stack.peek()],nums[i])){
                int index = stack.pop();
                result[index] = i;
            }
            stack.push(i);
        }
        return result;
    }    
}
/* 
┌─────────────────────┬────────────────┬───────────────┐
│ Goal                │ Stack Type     │ Direction     │
├─────────────────────┼────────────────┼───────────────┤
│ Next Greater Right  │ Decreasing     │ Left → Right  │
│ Next Smaller Right  │ Increasing     │ Left → Right  │
│ Next Greater Left   │ Decreasing     │ Right → Left  │
│ Next Smaller Left   │ Increasing     │ Right → Left  │
└─────────────────────┴────────────────┴───────────────┘

Pop condition: Violate stack property
  Decreasing stack → pop when stack[-1] <  current
  Increasing stack → pop when stack[-1] >  current
*/