import java.util.*;

class Solution {
    boolean solution(String s) {
        List<Character> list = new ArrayList<>();
        
        for (char word : s.toCharArray()) {
            if (word == '(') {
                list.add(word);
            } else {
                if (list.isEmpty()) return false;
                
                list.remove(list.get(list.size()-1));
            }
        }
        
        if (list.isEmpty()) return true;
        else return false;
    }
}