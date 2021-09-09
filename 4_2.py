from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(val):

    for el in content.split('</NumCode><CharCode>'):
        if el[:3] == val.upper():
            return float(el.split('</Name><Value>')[-1][:7].replace(',', '.'))


print(f'Курс USD = {currency_rates("USD")}')
print(f'Курс gbp = {currency_rates("gbp")}')
print(f'Курс aaa = {currency_rates("aaa")}')