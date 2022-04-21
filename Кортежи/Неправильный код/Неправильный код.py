import random


def change(nums):
    nums_l = list(nums)
    index = random.randint(0, 4)
    print(f'index {index}')
    value = random.randint(100, 1000)
    nums_l[index] = value
    nums = tuple(nums_l)
    return nums, value


my_nums = 1, 2, 3, 4, 5
num_1 = change(my_nums)
num_2 = change(my_nums)


print(f'Кортеж № 1 {num_1[0]} и случайное значение {num_1[1]}')
print(f'Кортеж № 2 {num_2[0]} и случайное значение {num_2[1]}')
print(f'сумма первого  и второго случайного значения = {num_1[1] + num_2[1]}')
