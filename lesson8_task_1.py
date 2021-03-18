import re


def email_parse(email_address):
    try:
        RE_ADDRESS = re.compile(r'\w+@\w+\.\w{2,}')
        assert RE_ADDRESS.match(email_address), f'wrong{email_address}'
        RE_ADDRESS_PARS_USERNAME = re.compile(r'\w+')
        RE_ADDRESS_PARS_DOMAIN = re.compile(r'\w+\.\w{2,}')
        user = RE_ADDRESS_PARS_USERNAME.findall(email_address)
        domain = RE_ADDRESS_PARS_DOMAIN.findall(email_address)
        main_dict = {'username': user[0], 'domain': domain[0]}
        print(main_dict)
    except AssertionError:
        raise ValueError(f'wrong email: {email_address}')


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
