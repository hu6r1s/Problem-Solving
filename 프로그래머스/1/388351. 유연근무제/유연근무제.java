class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int cnt = 0;
        
        for (int i = 0; i < schedules.length; i++) {
            int hour = schedules[i] / 100;
            int minutes = schedules[i] % 100 + 10;
            
            if (minutes >= 60) {
                minutes %= 60;
                hour += 1;
            }
            int workTime = hour * 100 + minutes;
            
            if (output(workTime, timelogs[i], startday)) {
                cnt += 1;
            }
        }
        
        return cnt;
    }

    public boolean output(int workTime, int[] time, int startday) {            
        for (int i = 0; i < time.length; i++) {
            if (startday == 6 || startday == 7) {
                startday = (startday % 7) + 1;
                continue;
            }
            if (workTime < time[i]) {
                return false;
            }
            startday = (startday % 7) + 1;
        }
        return true;
    }
}

/*
시와 분은 100을 나눈 몫과 나머지로
1월, 2화, 3수, 4목, 5금, 6토, 7일
schedules[i]를 인정시간으로 바꾸기
돌면서 schedules[i] + 10보다 
*/