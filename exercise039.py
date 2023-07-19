# My answer
money = int(input('Type your amount money as a integer number ex 12500: '))
roi = float(input('What is the ROI? ex 3.5:  '))
yearsTime = int(input('For how many years do you want? '))


def calculateRoi(amt, roi, years):
    counter = 0
    total = amt
    interest = 0
    while not counter == years:
        interest = total * (roi / 100)
        total += interest
        counter += 1
    return total


print('\n', ('-' * 33))
print(f'| In {yearsTime} years,\n| With a ${money} starting money,\n| On a ROI of: {roi}% by year,\n| You will get on total: ${round(calculateRoi(money, roi, yearsTime), 2)}')
print('', ('-' * 33))

print()

# Solution
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value, 2))
