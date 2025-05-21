def solution(data, ext, val_ext, sort_by):
    idx = ['code', 'date', 'maximum', 'remain']
    data = list(filter(lambda x: x[idx.index(ext)] < val_ext, data))
    return sorted(data, key=lambda x: x[idx.index(sort_by)])
