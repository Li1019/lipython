# =======================
# error_log
# Author : Li
# 2022/04/18
# 18:11
encoding = 'utf-8'
# =======================

# try except can get error log
# at least 1 except
#
# while True:
#     try:
#         division_num = int(input('Please input a number:'))
#         print(1/division_num)
#     # except ZeroDivisionError:
#     #     print('0 cannot be division')
#     # except ValueError:
#     #     print('your input is not number')
#     except:  # 不指定error类型，get all error type
#         print('something went wrong in code')
#     else:  # 程序运行没问题则执行这句
#         print('correct')
#         break
#     finally:
#         print('running is done')

# 查找父类
# print(Exception.__bases__)
# Typical error
# NameError: 未定义的变量
# IndexError: 下标越界, index out of range
# FileNotFoundError : cannot find the file
# FileExistsError : file already exists

# try:
#     raise IOError  # manually report a error
# except IOError:
#     print('There is a IOError')


# log
# log level: debug <info < warning < error < critical
from loguru import logger  # side-package, need to install

# logfile = './log1_20220418.log'
# logger.remove(handler_id=None)  # DON'T PRINT IN terminal
# logger.add(logfile)  # 把log写到文件里

# logger.debug('松青')
# logger.info('test')
# logger.warning('test')
# logger.error('test')
# logger.critical('test')

logfile2 = './log2_20220418.log'
logger.remove(handler_id=None)
logger.add(logfile2, rotation='200KB', compression='zip')  # rotation = 200KB, 指定log文件的最大size, compression指定压缩格式


# for i in range(10000):
#     logger.warning('test')

def fun1(a, b):
    return a / b


try:
    print(fun1(10, 0))
except:
    logger.exception('Error!!')  # exception is Error level
