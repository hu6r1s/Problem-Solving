def solution(m, musicinfos):
    def convert_sharp(s):
        return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace('B#','b')
    
    def time_to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    
    
    answer = "(None)"
    m = convert_sharp(m)
    max_play = 0
    
    for idx, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        melody = convert_sharp(melody)
        time_diff = time_to_min(end) - time_to_min(start)
        
        if time_diff > len(melody):
            played = (melody * (time_diff // len(melody))) + melody[:time_diff % len(melody)]
        else:
            played = melody[:time_diff]
        
        if m in played:
            if time_diff > max_play:
                answer = title
                max_play = time_diff
        
    return answer