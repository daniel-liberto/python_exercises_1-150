# My answer
from datetime import datetime
currentDate = str(datetime.now()).split()
currentTime = currentDate[1].split(sep='.')
print('Today is:', currentDate[0], 'and the time now is:', currentTime[0])

print()

# Solution
# import datetime
now = datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# some anotations
# %Y: year with century as a decimal number.
# %m: month as a zero-padded decimal number.
# %d: day of the month as a zero-padded decimal number.
# %H: hour (24-hour clock) as a zero-padded decimal number.
# %M: minute as a zero-padded decimal number.
# %S: second as a zero-padded decimal number.
