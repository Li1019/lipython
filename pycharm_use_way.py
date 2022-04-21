# encoding=utf-8

# settings>Editor>file and code template
# =======================
# 123
# Author : Li
# 2022/04/14
# 16:25
encoding = 'utf-8'


# =======================

# # settings>Editor>live template, apply to python
# def sum_data(num1, num2):
#     return num1 + num2
#
#
# print(sum_data(1, 111))

# change color, settings>Editor>color and scheme > python > line comment

# easy way to fix code format: command+option+l, windows: control+alt+l

# physical environment, virtual environment, can select when create new project

# Split screen, Settings > Keymap > right top to search split to change shotcut

# file encoding setting , settings>File Encoding to change OR add at the 1st line of file #encoding=utf-8


# Bubble algorithm

def bubble_algo(compare_num):
    list1 = []
    for i in range(0, compare_num):
        value = int(int(input('please input 5 numbers:')))
        list1.append(value)

    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)


bubble_algo(5)
