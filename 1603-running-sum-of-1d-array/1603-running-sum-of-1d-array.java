class Solution {
    public int[] runningSum(int[] nums) {
        int sum_cnt = 0;
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            sum_cnt += nums[i];
            result[i] = sum_cnt;
        }
        return result;
    }
}