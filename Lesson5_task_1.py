def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


print(type(odd_nums(15)), *odd_nums(15))
