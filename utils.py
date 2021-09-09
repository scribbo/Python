from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(val):

    for el in content.split('</NumCode><CharCode>'):
        if el[:3] == val.upper():
            return float(el.split('</Name><Value>')[-1][:7].replace(',', '.'))


if __name__ == '__main__':
   print("I'm utils.py")
else:
    print("I'm a module")


currency_rates('usd')