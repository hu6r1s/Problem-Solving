class Solution {
    public int[][] solution(int n) {
        int num = 1;
        int colStart = 0;
        int colEnd = n-1;
        int rowStart = 0;
        int rowEnd = n-1;
        int[][] board = new int[n][n];
        while (num <= n * n) {
            for (int i = colStart; i <= colEnd; i++) {
                board[rowStart][i] = num++;
            }
            rowStart++;
            for (int i = rowStart; i <= rowEnd; i++) {
                board[i][colEnd] = num++;
            }
            colEnd--;
            for (int i = colEnd; i >= colStart; i--) {
                board[rowEnd][i] = num++;
            }
            rowEnd--;
            for (int i = rowEnd; i >= rowStart; i--) {
                board[i][colStart] = num++;
            }
            colStart++;
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