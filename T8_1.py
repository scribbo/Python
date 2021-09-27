import re


def email_parse(email):

    try:
        username = re.compile(r'^(\w+)@(\w+.\w+)')
        domain = re.compile(r'@(\w+.\w+)')

        return {'username': username.findall(email)[0], 'domain': username.findall(email)[1]}

    except ValueError:
        print(f"wrong email: {email}")


print(email_parse('sdbb@mail.ru'))
