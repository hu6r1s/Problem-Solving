class Solution {
    public int[] solution(int[] num_list) {
        int[] result = new int[num_list.length + 1];
        System.arraycopy(num_list, 0, result, 0, num_list.length);
        if (num_list[num_list.length - 1] > num_list[num_list.length - 2]) {
            result[num_list.length] = num_list[num_list.length - 1] - num_list[num_list.length - 2];
        } else {
            result[num_list.length] = num_list[num_list.length - 1] * 2;
        }
        return result;
    }
}