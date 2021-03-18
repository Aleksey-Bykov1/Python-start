from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f'{func.__name__} ({", ".join(map(str, args))}: {type(*args)})')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(8.2)
b = calc_cube(3)
c = calc_cube(1234)
print(a, b, c)



