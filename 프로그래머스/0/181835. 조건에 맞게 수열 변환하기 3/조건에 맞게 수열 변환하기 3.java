import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        if (k % 2 == 1) {
            return Arrays.stream(arr).map(a -> a * k).toArray();
        } else {
            return Arrays.stream(arr).map(a -> a + k).toArray();
        }
    }
}