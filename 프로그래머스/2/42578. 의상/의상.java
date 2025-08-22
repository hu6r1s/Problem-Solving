import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        int result = 1;
        
        for (String[] cloth : clothes) {
            map.put(cloth[1], map.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (int v : map.values()) {
            System.out.println(v);
            result *= v + 1;
        }
        return result - 1;
    }
}