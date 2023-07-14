# My answer
import calendar

year = int(input("Type selected year: "))
month = int(input("Type selected month: "))

print('\n', calendar.month(year, month))

print()

# Solution
# import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
