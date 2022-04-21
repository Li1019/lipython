# =======================
# summary
# Author : Li
# 2022/04/15
# 8:12
encoding = 'utf-8'
# =======================

# string
# str1 = 'automation'
# str2 = 'I like'
# print(f'{str2} : {str1}')
# print(f'{str2:020} : {str1:040}') # str右边以0补齐20，40位
# # str3 = f'{str2:<20} : {str1:<40}' # 右边以空格补齐
# str3 = f'{str2:>20} : {str1:>40}' # 左边以空格补齐
# print(str3)

# str1 = 'automationpython'
# str2 = str1[0:10]  # automation
# str3 = str1[-16:-6]  # automation
# str4 = str1[3:0:-1] # otu
# str5 = str1[::-1] # 反转
# print(str5)

# list
# list1 = [3, 10, 1, 393, -21, 90]


# list1.sort() # ASC, it's operation, no return value, chang original sort
# print(list1)
# list1_new = sorted(list1) # ASC, create a new list, list1 is no change
# print(list1)
# print(list1_new)

# list1.sort(reverse=True) #DESC
# print(list1)

# list1_new_2 = sorted(list1, reverse=True)  # DESC
# print(list1)
# print(list1_new_2)

# check string is 回文
# def check_str(str):
#     if str == str[::-1]:
#         print('yes')
#     else:
#         print('no')
#
#
# str1 = input('please input a string:')
# check_str(str1)


# update list
# list2 = [100, 200, 300]
# val = 400
# list2.append(val) # add item at the end of list
# list2.insert(1, val)  # add item to any location
# list_new = [500, 600]
# list2.extend(list_new)  # extend <- combine multiple list
# print(list2)

# delete list
# list2 = [100, 200, 300]

# list2.pop(0)  # delete index list's value
# list2.remove(300)  # delete specific value in the list
# del list2[0:1] # delete list a range of values, parameter
# del list2  # delete whole list
# print(list2)


# 打印斐波那契数列的前n位
# 1, 1, 2, 3, 5, 8, 13, 21, 34...
# def fun1(n):
#     list1 = []
#     for i in range(n):
#         if i < 2:
#             list1.append(1)
#         else:
#             list1.append(list1[i - 2] + list1[i - 1])
#     return list1
#
#
# n = int(input('please input a number:'))
# print(fun1(n))

# tuple
# immutable object, can use index and split
# if only 1 item in tuple, need to add "," at the end
# sub-list in tuple, can update the sub-list

# copy and deepcopy
# copy -> only copy list, sub-list is not copied
# deep copy -> copy list and all sub-list
# assign value is just give a different name, but value is totally same

# list1 = [100, 200, 300, [666, 888]]

# list2 = list1  # a different name, but same list
# list1[0] = 900  # list1 and list2, both are changed

# import copy
#
# # list2 = copy.copy(list1)
# # list2[0] = 900
# # list2[3][0] = 222
#
# list2 = copy.deepcopy(list1)
# list2[0] = 900
# list2[3][0] = 222
#
# print(list1)
# print(list2)

# function
# def func1(n):
#     sum1 = 0
#     for i in range(1, n + 1):
#         sum1 += i
#     return sum1
#
#
# print(func1(100))

# don't use loop to calculate n! 递归
# n! = n*(n-1)!

# def func2(n):
#     if n == 1:
#         return 1
#     elif n > 6:
#         print('number is too big, cannot do calucate')
#     else:
#         return n*func2(n-1)
#
#
# print(func2(6))


# else in loop
# if no 'break' in loop, then will run 'else' part after loop is done
# def func3(n):
#     sum2 = 0
#     for i in range(1, n + 1):
#         sum2 += i
#     else:
#         print("I calculated all numbers' sum")
#     return sum2
#
# print(func3(100))

# file write
# w+ read/write, if no this file, will create one and clear existed content
# r+ read/write, if no this file, then error, cover write from begging (not clear)
# a+ read/write, if no this file, will create one , add content to the end

# file read
# file.readline(), read 1 line, return is string
# file.readlines(), read whole content, return is list, 1 line is one element in list
# file.read().splitlines() read whole content, return is list, 1 line is 1 element, no '\n'

# path = '/Users/lipan/PycharmProjects/pythonProject/file_test.txt'
# with open(path, 'w+', encoding='utf-8') as file1:
#     file1.write('456')
#     file1.seek(0)
#     print(file1.read())

# with open(path, 'r+', encoding='utf-8') as file1:
#     file1.write('123')
#     file1.seek(0)
#     print(file1.readline())


# with open(path, 'a+', encoding='utf-8') as file1:
#     file1.write('x')
#     file1.seek(0)
#     print(file1.readline())


# with open(path, encoding='utf-8') as file2:
#     list4 = file2.read().splitlines()
#     i = 0
#     for i in range(len(list4)):
#         str1 = list4[i]
#         name1 = str1.split(',')[0].split(':')[1].strip()
#         age1 = str1.split(',')[1].split(':')[1].strip()
#         print(f'{name1},{age1}')
#
# # import pathlib
# # print(__file__)

# dict
# dict doesn't have order, always pair: key, value
# dict1 = {'A': 'Apple', 'B': 'Baby', 'C': 'Circle'}

# print(dict1['A'])  # print key's value
# dict1['B'] = 'Bento' # has key in dict, then update the value
# print(dict1['B'])
# dict1['D'] = 'Detail' # doesn't have key 'D', then append it to dict
# print(dict1['D'])
# print('A' in dict1) # return boole, check weather has the key in dict
# print('Apple' in dict1) # return false, check with key, not value
# del dict1['D']
# print(dict1['D'])
# dict1.clear()  # ip_address is not changed
# dict2 = {}  # create a new dict

# traverse dict
# for key in dict1.keys():
#     print(key)
#
# for value in dict1.values():
#     print(value)
#
# for key,value in dict1.items():
#     print(key, value)

# import random
#
# with open(path, 'w+', encoding='utf-8') as account_file:
#     for i in range(0, 1000):
#         account = f'sq{i:03}, '
#         password = random.randint(0, 999999)
#         if password < 100000:
#             password = f'{password:06}'
#         if i < 999:
#             account_file.write(f'{account}{password}\n')
#         else:
#             account_file.write(f'{account}{password}')


# json
# json is string in python
# str1 = '''{
# "aa001": "张三",
# "ac001": "07041225252",
# "crm003": "1",
# "crm004": "1"
# }'''
# # make sure json format is correct, if not, error occurs
#
# # login page, post a json, tel number is unique, and change it to random.
# import json
# from random import randint
# dict1 = json.loads(str1)  # change json file to dict
# dict1['ac001'] = f'070{randint(10000000,99999999)}'
# str1 = json.dumps(dict1,ensure_ascii=False)
# print(str1)


# request 爬虫: copy text from webpage
import re  # 正则表达式
#
# str1 = 'Ilovepython3Iloveppython3'
# str1_new = re.findall('p(.*?)3', str1)  # return is list
# print(str1_new)

import requests  # 爬虫 site-package

# url = 'https://www.linebook.org/books/33008218/'
# path = '/Users/lipan/PycharmProjects/pythonProject/file_requests.txt'
#
# req = requests.get(url, headers={'User-Agent': 'Chrome'})
# # req = requests.get(url)  # get req.status_code = 520, add headers={'User-Agent': 'Chrome'} can solve it.
# print(req.status_code)
# html_text = req.text
# # print(html_text)  # get webpage content (html)
# book_name = re.findall('<h1>(.*?)</h1>', html_text)
# item_name_list = re.findall('title="我活了几千年林羽小说(.*?)</a>', html_text)
# html_url_category_list = re.findall('href="(.*?).html', html_text)
# dict1 = {}
#
# with open(path, 'w+', encoding='utf-8') as file_request:
#     for i in range(len(item_name_list)):
#         str_item_name = item_name_list[i]
#         str_item_name = str_item_name.split('">')[0]
#         # print(str_item_name)
#         # write_str_item_name = f'{str_item_name}\n'
#         # file_request.write(write_str_item_name)
#         str_url_category = html_url_category_list[i]
#         dict1[str_item_name] = f'https://www.linebook.org{str_url_category}.html'
#         write_content = f'{str_item_name},{str_url_category}\n'
#         file_request.write(write_content)

# 跨行匹配
# str1 = '''ilowpython
# iloveautomation1
# jmeter2'''
#
# # str_new = re.findall('1(.*?)2', str1)
# # print(str_new)  # result is [], can't get value, because '2' is in a new line
# str_new = re.findall('1(.*?)2', str1, re.S)  # get value in multiple lines
# print(str_new)
