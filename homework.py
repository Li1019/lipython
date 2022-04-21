# =======================
# homework
# Author : Li
# 2022/04/18
# 17:53
encoding = 'utf-8'
# =======================

# 猜数字游戏，最多猜7次

from random import randint

random_number = randint(0, 100)

for i in range(7):
    input_num = int(input('please input the number: '))
    if (input_num < random_number):
        print('Your number is small')
    elif (input_num > random_number):
        print('Your number is big')
    else:
        print('You are correct')
        break
