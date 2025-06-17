import java.util.*;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        List<String> answer = new ArrayList<>();
        
        for (int i = 0; i < todo_list.length; i++) {
            if (!finished[i]) {
                answer.add(todo_list[i]);
            }
        }
        return answer.toArray(new String[0]);
    }
}

// for문 돌면서 finished가 false인 인덱스만 따로 배열