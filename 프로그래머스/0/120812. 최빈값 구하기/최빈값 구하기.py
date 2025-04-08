def solution(array):
    c_arr = dict.fromkeys(array)
    for key in c_arr.keys():
        c_arr[key] = array.count(key)
    
    k_arr = [k for k, v in c_arr.items() if c_arr[k] == max(c_arr.values())]
    return -1 if len(k_arr) > 1 else k_arr[0]