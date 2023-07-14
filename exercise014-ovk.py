# My answer
from datetime import date
import re

date1, date2 = '', ''
regex = re.compile(
    r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$')
result = 'bazinga'


def number_of_days(regex, date1, date2):
    date1 = str(input('Enter first date: year/month/day\n'))
    date2 = str(input('Enter second date: year/month/day\n'))
    if re.fullmatch(regex, date1) and re.fullmatch(regex, date2):
        date1 = date.fromisoformat(date1.replace('/', '-'))
        date2 = date.fromisoformat(date2.replace('/', '-'))
        result = (date2 - date1).days
        print('\nFirst date choosen: ', date1)
        print('Second date choosen: ', date2)
        print('Numbers of days between two dates are:', result, 'days')
        quit()
    else:
        print('\n' * 5, 'Wrong format! type again.')
        result = ''
    return result


while result == 'bazinga':
    number_of_days(regex, date1, date2)

print()

# Solution
# from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
