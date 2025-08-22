import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        
        for (int a : arr) {
            if (!answer.isEmpty() && a == answer.get(answer.size() - 1)) {
                continue;
            }
            answer.add(a);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}