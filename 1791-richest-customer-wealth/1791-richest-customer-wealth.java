import java.util.*;

class Solution {
    public int maximumWealth(int[][] accounts) {
        int result = 0;
        for (int i = 0; i < accounts.length; i++) {
            int max_num = Arrays.stream(accounts[i]).sum();

            if (result < max_num) {
                result = max_num;
            }
        }
        return result;
    }
}