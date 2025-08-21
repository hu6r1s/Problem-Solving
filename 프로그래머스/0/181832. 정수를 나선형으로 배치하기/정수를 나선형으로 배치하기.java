class Solution {
    public int[][] solution(int n) {
        if (n == 1) {
            return new int[][]{{1}};
        }
        
        char direction = 'r';
        int x = 0;
        int y = 0;
        int[][] board = new int[n][n];
        for (int i = 0; i < n * n; i++) {
            board[x][y] = i + 1;
            if (direction == 'r') {
                y++;
                if (y == n-1 || board[x][y+1] != 0) {
                   direction = 'd';
                }
            } else if (direction == 'd') {
                x++;
                if (x == n-1 || board[x+1][y] != 0) {
                   direction = 'l';
                }
            } else if (direction == 'l') {
                y--;
                if (y == 0 || board[x][y-1] != 0) {
                   direction = 'u';
                }
            } else if (direction == 'u') {
                x--;
                if (x == 0 || board[x-1][y] != 0) {
                   direction = 'r';
                }
            }
        }
        return board;
    }
}

/*
4
 1  2  3 4
12 13 14 5
11 16 15 6
10  9  8 7
00 01 02 03 13 23 33 32 31 30 20 10 11 12 22 21 

*/