# from math import*
# number1 = int(input('Enter fisrt number '))
# number2 = int(input('Enter second number '))
# sum = number1 + number2
# product = number1*number2
# print("Sum of that is ",sum)
# print("Product of that is ",product)
# print("module of number one", abs(number1))
# print("module of number two", abs(number2))

# length = float(input('enter your length ')) / 100
# print(length, 'in metr')
import math

# num1 = int(input('a = '))
# num2 = int(input('b = '))
# a = num1 % num2  # Remainder
# b = math.floor(num1 / num2)  # Quotient (floored)
# print('qoldiq', a)  # Prints the remainder
# print('butun', b)   # Prints the quotient


num = int(input('enter number '))

first = math.floor(num / 100)
second = math.floor((num % 100) / 10) 
third = math.floor(num % 10)

result = first + second + third
print('result ', result)