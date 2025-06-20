import java.util.*;

class Solution {
    public int solution(int n, String control) {
        for (char w : control.toCharArray()) {
            switch (w) {
                case 'w': n += 1; break;
                case 's': n -= 1; break;
                case 'd': n += 10; break;
                case 'a': n -= 10; break;
            }
        }
        
        return n;
    }
}