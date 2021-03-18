from functools import wraps


def val_checker(v_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            if v_func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(7)
    b = calc_cube(-3)
except ValueError as f:
    print(f)
