sym_list = ['a', 'b', 'c']
for num, sym in enumerate(sym_list):
    print(f'{num + 1}-й номер со значением: {sym}')

print('\n*******************\n')

gen = enumerate(sym_list)
print(type(gen))
print(gen)  # enumerate object at

print('\n*******************\n')

gen = enumerate(sym_list)
print(tuple(gen))


print('\n*******************\n')

gen = enumerate(sym_list)
[print(i) for i in gen]
