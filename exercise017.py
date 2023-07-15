# My answer
inputNumber = int(input('Type a number between 1 and 3000: '))

if inputNumber <= 550:
    print(f'The number "{inputNumber}" is more close to 100')
elif inputNumber > 551 and inputNumber <= 1500:
    print(f'The number "{inputNumber}" is more close to 1000')
else:
    print(f'The number "{inputNumber}" is more close to 2000')

print()

# Solution? i've definitely misunderstood the question.


def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
