def print_hello(name):
    print(f'hello {name}')

def make_sum(num1,num2):
    sum_total = num1 + num2
    return sum_total

print(__name__)  # if run this in current module, result is __main__, if not, it's module_1.module_test
if __name__ == '__main__':
    print('you are a good guy')
    print(__name__)  # __main__