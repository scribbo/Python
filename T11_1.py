class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def num_date(cls, obj):
        my_date = obj.date.split('-')
        print(f'number = {int(my_date[0])}, month = {int(my_date[1])}, year = {int(my_date[2])}')

    @staticmethod
    def correct_date(obj):
        my_date = obj.date.split('-')
        list_31 = [1, 3, 5, 7, 8, 10, 12]
        d = int(my_date[0])
        m = int(my_date[1])
        y = int(my_date[2])
        if m == 2 and y % 4 == 0 and d > 29:
            print('There are only 29 days in February of a leap year')
        elif m == 2 and y % 4 != 0 and d > 28:
            print('There are only 28 days in February of a common year')
        elif m in list_31 and 1 <= d <= 31 and y > 0:
            print('The date is correct')
        elif m not in list_31 and 1 <= d <= 30 and y > 0:
            print(f'The date is correct')
        else:
            print('The date is not correct')


a = Date('35-03-2021')
b = Date('01-04-2015')
Date.num_date(a)
Date.correct_date(a)
Date.num_date(b)
Date.correct_date(b)
