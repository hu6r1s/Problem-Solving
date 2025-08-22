import java.util.*;

class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        
        for (int num : nums) {
            numSet.add(num);
        }
        
        if (numSet.size() > nums.length / 2) {
            return nums.length / 2;
        }
        
        return numSet.size();
    }
}