class OwnError(Exception):

    @staticmethod
    def m_1(p_1, p_2):
        try:
            p_1, p_2 = map(int, (p_1, p_2))
            if p_2 == 0:
                raise OwnError("Второе число не должно быть нулем")
        except ValueError:
            print('Вы ввели не число')
        except OwnError as err:
            print(err)
        else:
            print(f'Результат {p_1 / p_2:.2f}')


one = OwnError.m_1(5, '0')

