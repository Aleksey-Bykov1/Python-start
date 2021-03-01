def odd_nums(n):
    result = (i for i in range(1, n + 1, 2))
    return result


print(type(odd_nums(15)), *odd_nums(15))
