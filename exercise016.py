# My answer
inputNumber = int(input('Enter a integer number: '))

if inputNumber <= 17:
    print(
        f'The difference between "{inputNumber}" and "17" are: {17 - inputNumber}')
else:
    print(
        f'The difference between "{inputNumber}" and "17" are: {abs(17 - inputNumber) * 2}, with double penalization, because it\'s above 17.')

print()

# Solution


def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(22))
print(difference(14))
