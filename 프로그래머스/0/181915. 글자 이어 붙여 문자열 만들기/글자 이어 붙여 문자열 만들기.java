import java.util.*;

class Solution {
    public String solution(String my_string, int[] index_list) {
        String result = "";
        for (int idx : index_list) {
            result += my_string.charAt(idx);
        }
        return result;
    }
}