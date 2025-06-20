class Solution {
    public String solution(int[] numLog) {
        String result = "";
        
        for (int i = 0; i < numLog.length - 1; i++) {
            int diff = numLog[i+1] - numLog[i];
            if (diff == 1) {
                result += "w";
            } else if (diff == -1) {
                result += "s";
            } else if (diff == 10) {
                result += "d";
            } else {
                result += "a";
            }
        }
        return result;
    }
}