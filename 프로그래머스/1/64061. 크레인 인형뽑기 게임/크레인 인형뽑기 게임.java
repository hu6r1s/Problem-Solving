import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        ArrayList<Integer> stack = new ArrayList<>();
        int cnt = 0;
        
        for (int move : moves) {
            for (int i = 0; i < board.length; i++) {
                if (board[i][move-1] != 0) {
                    int doll = board[i][move-1];
                    board[i][move-1] = 0;
                    
                    if (!stack.isEmpty() && stack.get(stack.size()-1) == doll) {
                        stack.remove(stack.size()-1);
                        cnt += 2;
                    } else {
                        stack.add(doll);
                    }
                    break;
                }
            }
        }
        return cnt;
    }
}


/*
0 0 0 0 0
0 0 0 0 0
0 0 5 0 0
0 2 4 0 2
0 5 1 3 1

[4, 2, 4]
2
*/