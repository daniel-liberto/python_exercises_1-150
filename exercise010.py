# My answer
n = int(input('Enter a integer number: '))
result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(result)

print()

# Solution
a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1+n2+n3)
