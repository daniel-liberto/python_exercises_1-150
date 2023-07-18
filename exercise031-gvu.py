# My answer(i gave up on this one, so much time for a niche thing)
firstNum = int(input('Type first integer number: '))
secondNum = int(input('Type second integer number: '))


def gcdCalc(num):
    aux = []
    while not num == 1:
        if not num / 2 == 1 and num % 2 == 0:
            num / 2
            aux += 2
        elif not num / 3 == 1 and num % 2 == 0:
            num / 3
            aux += 3
        elif not num / 5 == 1 and num % 2 == 0:
            num / 5
            aux += 5


print()

# Solution


def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))
print("GCD of 336 & 360 =", gcd(336, 360))
