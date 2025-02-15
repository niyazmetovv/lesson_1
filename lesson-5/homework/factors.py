positive_number = int(input("Enter a positive integer: "))
print(*(f"{n} is factor of {positive_number}" for n in range(1, positive_number+1) if positive_number % n == 0), sep = '\n')