class ListErr(Exception):

    def input_data(self):
        return print(self)


nums = []
while True:
    try:
        num = input("Введите число или stop для остоновки ввода: ")
        if num.isdigit():
            nums.append(int(num))
        elif num == 'stop':
            break
        else:
            raise ListErr("Вы ввели не число")
        continue
    except ListErr as err:
        print(err)

ListErr.input_data(nums)
