import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> days = new ArrayList<>();
        
        for (int i = 0; i < speeds.length; i++) {
            days.add((int) Math.ceil((100.0 - progresses[i]) / speeds[i]));
        }
        
        int cnt = 0;
        int curDay = days.get(0);
        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i < days.size(); i++) {
            cnt += 1;
            if (curDay < days.get(i)) {
                answer.add(cnt);
                cnt = 0;
                curDay = days.get(i);
            }
        }
        answer.add(cnt+1);
        return answer.stream().mapToInt(i -> i).toArray();
    }
}