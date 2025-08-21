class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[][] keypad = {
            {3, 1},
            {0, 0}, {0, 1}, {0, 2},
            {1, 0}, {1, 1}, {1, 2},
            {2, 0}, {2, 1}, {2, 2}
        };
        
        int[] left = {3, 0};
        int[] right = {3, 2};
        
        for (int number : numbers) {
            if (number == 1 || number == 4 || number == 7) {
                answer += "L";
                left[0] = keypad[number][0];
                left[1] = keypad[number][1];
            } else if (number == 3 || number == 6 || number == 9) {
                answer += "R";
                right[0] = keypad[number][0];
                right[1] = keypad[number][1];
            } else {
                int ldist = Math.abs(keypad[number][0] - left[0]) + Math.abs(keypad[number][1] - left[1]);
                int rdist = Math.abs(keypad[number][0] - right[0]) + Math.abs(keypad[number][1] - right[1]);
                
                if (ldist < rdist) {
                    answer += "L";
                    left[0] = keypad[number][0];
                    left[1] = keypad[number][1];
                } else if (ldist > rdist) {
                    answer += "R";
                    right[0] = keypad[number][0];
                    right[1] = keypad[number][1];
                } else {
                    if (hand.equals("right")) {
                        answer += "R";
                        right[0] = keypad[number][0];
                        right[1] = keypad[number][1];
                    } else {
                        answer += "L";
                        left[0] = keypad[number][0];
                        left[1] = keypad[number][1];
                    }
                }
            }
        }
        return answer;
    }
}


/*
현재 방식은 분기와 키패드의 차이를 이용했는데 차이로는 거리를 잡지 못함.
맨허튼 거리 방식이 있음. |x1 - x2| + |y1 - y2|
*/