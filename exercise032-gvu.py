# My answer (it's the same thing from before)
firstNum = int(input('Type first integer number: '))
secondNum = int(input('Type second integer number: '))


def lcmCalc(num1, num2):
    while not num1 == 1 and not num2 == 1:
        if num1 % 2 == 0:
            print()


print()

# Solution


def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while (True):
        if ((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm


print(lcm(4, 6))
print(lcm(15, 17))
