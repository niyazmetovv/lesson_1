#1
name = input("Enter your name: ")
yearOfBirth = input("Enter your age: ")
yearOfBirth = int(yearOfBirth)
age = 2025 - yearOfBirth
print ("Your name is", name, "and you are", age, "years old")

#2

txt = 'LMaasleitbtui'
print('tesla')

#3

str = input("Enter a string: ")
print(len(str))
print(str.upper())
print(str.lower())

#4
str1 = str.lower()
if str1 == str1[::-1]:
    print("Yes")
else:
    print("No")

#5

str2 = input("Enter a string: ")
lowStr2 = str2.lower()
vowels = "aeoui"
counterV = 0
counterC = 0
for s in lowStr2:
        if s in vowels:
            counterV += 1
        elif s.isalpha():
            counterC += 1

print(counterV, counterC)

#6

a = int(input("Enter first string: "))
b = int(input("Enter second string: "))

if a in b:
    print("Yes")
else:
    print("No")


#7

sentence = input("Enter sentence: ")
replace = input("Enter replacement: ")
withSentence = input("Enter sentence: ")
result = sentence.replace(replace, withSentence)
print(result)


#8

smth = input("Enter string: ")
print(f"first letter: {smth[0]}, last letter: {smth[-1]}")

#9

smth2 = input("Enter string: ")
print(f"reversed: {smth2[::-1]}")

#10

smth3 = input("Enter string: ")
print(len(smth3.split()))

#11

for s in smth3:
    if s.isdigit():
        print("Yes")
        break
    else:
        print("No")

#12

words = input("Enter words: ").split()
seperator = input("Enter separator: ")
resultString = ""
for w in range(len(words)):
    resultString += words[w]
    if w != len(words)- 1:
        resultString += seperator
print(resultString)

#13

str13 = input("Enter a string: ")
resultString13 = str13.replace(" ", "")
print(resultString13)

#14

str14 = input("Enter a string: ")
str15 = input("Enter a string: ")
if str14 == str15:
    print("Yes")
else:
    print("No")

#15

str16 = input("Enter a string: ")
wordsOfStr16 = str16.split()

resultString16 = ""

for s in wordsOfStr16:
    resultString16 += s[0]
print(resultString16)

#16
str17 = input("Enter a string: ")
char17 = input("Enter a character: ")
resultString17 = ""
for s in range(len(str17)):
    if str17[s] != char17:
        resultString17 += str17[s]

print(resultString17)
#17

str18 = input("Enter a string: ")
vowels = "aeiou"
resultString18 = str18


for a in range(len(str18)):
    if str18[a] in vowels:
       resultString18 = resultString18.replace(str18[a], '*')
print(resultString18)

#18
dtr = input("Enter a string: ")
wordsOfStr19 = dtr.split()
print(f"Starts with: {wordsOfStr19[0]}, ends with: {wordsOfStr19[-1]}")