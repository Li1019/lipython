# import module_1

# import module from different directory
# from module_1 import module_test
# module_test.print_hello('li')
# print(module_test.make_sum(1,100))

# import module from same directory
# import main
# main.print_hi('Tompee')

# import arrow
# now = arrow.now()
# print(now)

# from pathlib import Path  # import from 3rd-part library
# print(Path(__file__)) # print current directory
# print(Path(__file__).parent)   # print current's parent directory
# print(__file__) # print current directory

# import standard directory (specific directory)
import sys
# for one in (sys.path):
#     print(one)

# add directory into starndard directory
# import sys
# sys.path.append('/Users/lipan/test_module')
# for one in (sys.path):
#     print(one)
# import test_1
# test_1.print_thanks('This is a test for append standard directory')

