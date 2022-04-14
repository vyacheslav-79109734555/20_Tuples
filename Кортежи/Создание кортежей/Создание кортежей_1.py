def add_num(seg, numb):
    seg = list(seg)
    for i_num in range(len(seg)):
        seg[i_num] += numb
    return seg


origin_tuple = (3, 1, 4, 1, 5)  # кортеж
changed_tuple = origin_tuple[:]  # срез от кортежа

print('\nсрез от кортежа', changed_tuple)
print('**', add_num(origin_tuple, 5))
