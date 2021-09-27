from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        my_list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({el}: {type(el)})' for el in my_list]
        print(*n)
    return wrapper


@type_logger
def calc_cube(*x, **y):
    my_list = [el for el in (*x, *y.values()) if type(el) == int or type(el) == float]
    return [el ** 3 for el in my_list]


calc_cube(5, 5.8, first='1')


