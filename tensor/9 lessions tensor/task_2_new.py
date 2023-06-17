import datetime


def func_log(file_log='log.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_log, 'a', encoding='utf-8') as f:
                f.write(f'{func.__name__} вызвана {datetime.datetime.now().strftime("%d.%m %H:%M:%S")}\n')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@func_log()
def my_func():
    print('Функция 1')


@func_log(file_log='my_func2.txt')
def my_func2():
    print('Функция 2')


my_func()
my_func2()
my_func()
