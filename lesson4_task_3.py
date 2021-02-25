
def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encoding)
    val = currency
    date = content[(content.find('Date')) + 6: (content.find('Date')) + 16]
    if val in content:
        usd = content[content.find(f'{val}'):]
        res = usd[: usd.find("Value") + 11]
        result = float(res[-5:].replace(',', '.'))
        print(f'{result}, {date}')
    else:
        print('None')


if __name__ == '__main__':
    from requests import get, utils
    currency_rates('EUR')
