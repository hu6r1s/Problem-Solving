class Solution {
    public int solution(String binomial) {
        String[] operate = binomial.split(" ");
        switch (operate[1]) {
            case "+": return Integer.parseInt(operate[0]) + Integer.parseInt(operate[2]);
            case "-": return Integer.parseInt(operate[0]) - Integer.parseInt(operate[2]);
            case "*": return Integer.parseInt(operate[0]) * Integer.parseInt(operate[2]);
        }
        return 0;
    }
}