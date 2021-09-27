from functools import wraps


def val_checker_l(lambda_func):
    def val_checker(func):

        @wraps(func)
        def wrapper(x):
            if lambda_func(x):
                print(func(x))
            else:
                raise ValueError(f'wrong value {x}')

        return wrapper

    return val_checker


@val_checker_l(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

calc_cube(5)