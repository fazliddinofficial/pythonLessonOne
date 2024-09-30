from math import*

# a = input('enter number a ')
# b = input('enter number b ') 
# c = int(a )** 2 + int(b )** 2
# print(f"{a} + {b} = {c ** 0.5}")


# pi = float(3.14)
# d = input('enter d')
# r = int(d) / 2
# result = pi * r ** 2
# print(result)

# x = int(input('Enter x '))
# y = ((1 + pow(x,4)) / (sin(x) + abs(x))) - tan(x)
# print(floor(y))

# x = int(input('enter x '))
# y = abs(1+pow(x,6)) / (sin(x) + sqrt(x))
# print(y)

# a = int(input('enter a '))
# b = int(input('enter b '))
# c = int(input('enter c '))
# t = int(input('enter t '))
# x = int(input('enter x '))

# first = ((a*pow(x,2))-(b*x)- c) / abs(x)
# second = abs((x-t)/sqrt(x+a))
# print(floor(first-second))

a = int(input('enter a '))
b = int(input('enter b '))
c = int(input('enter c '))
t = int(input('enter t '))
x = int(input('enter x '))

first = 2 / (abs( (a*pow(x,2)) - b*x) + c)

second = abs((x-t)/sqrt(x+a))

result = first - second

print(floor(result))


