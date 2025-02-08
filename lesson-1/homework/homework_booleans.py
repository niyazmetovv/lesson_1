#1

username = bool(input("Enter your username: "))
password = bool(input(("Enter your password: ")))
print(username and password)

#2

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a == b:
    print("equals")
else:
    print("not equals")

#3

c = int(input("Enter a number: "))

isPositiveAndEven = False
if c % 2 == 0 and c > 0:
    isPositiveAndEven = True
print(isPositiveAndEven)

#4

d = int(input("Enter first number: "))
e = int(input("Enter second number: "))
f = int(input("Enter third number: "))

areDifferent = False

if d != e and f != e and d != f:
    areDifferent = True
print(areDifferent)
#5

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
haveSameLength = False
if len(str1) == len(str2):
    haveSameLength = True
print(haveSameLength)

#6

g = int(input("Enter a number: "))
divisible = False

if g % 3 == 0 and g % 5 == 0:
    divisible = True
print(divisible)

#7

h = float(input("Enter a number: "))
i = float(input("Enter a number: "))
sum = i + h
greater = False
if sum > 50.8:
    greater = True
print(greater)

#7.2

j = float(input("Enter a number: "))
isBetween = False
if j >= 10 and j <= 20:
    isBetween = True
print(isBetween)