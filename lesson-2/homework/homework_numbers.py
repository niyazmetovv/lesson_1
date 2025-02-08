#first

a = float(input("enter a floating number: "))
print(f"{a:.2f}")

#second

b = int(input("enter first number: "))
c = int(input("enter second number: "))
d = int(input("enter third number: "))

max = max(b, c, d)
min = min(b, c, d)

print(max)
print(min)

#third

km = float(input("enter km: "))

meters = km * 1000
cm = meters * 100

print(f"meters: {meters}")
print(f"cm: {cm}")


#fourth

e = int(input("enter a first number: "))
f = int(input("enter a second number: "))

result = e//f
remainder = e % f

print(f"result: {result}")
print(f"remainder: {remainder}")


#fifth

celcius = float(input("enter celcius: "))
fahrenheit = celcius * 9 / 5 + 32
print(f"fahrenheit: {fahrenheit}")

#sixth

num = int(input("enter a number: "))
print(num%10)

#seventh

num2 = int(input("enter a number: "))
if num2 % 2 == 0:
    print("even")
else:
    print("odd")