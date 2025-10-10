def solution(files):
    arr = []
    result = []
    for file in files:
        num_start = 0
        while num_start < len(file) and not file[num_start].isdigit():
            num_start += 1
        
        num_end = num_start
        
        while num_end < len(file) and file[num_end].isdigit():
            num_end += 1
        
        arr.append((file[:num_start], file[num_start:num_end], file[num_end:]))
    
    arr.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for x, y, z in arr:
        result.append(x+y+z)
    return result


"""
파일명에 포함된 숫자를 반영한 정렬 기능 구현
대소문자 구분 안함
영문대소문자, 숫자, 공백, 마침표, 빼기 부호

"""