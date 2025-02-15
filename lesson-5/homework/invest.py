def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount *= (1 + rate)
        print(f"year {i}: ${amount:.2f}")







initial_amount = float(input("enter initial amount: "))
percentage = float(input("enter percentage rate: "))
number_of_years = int(input("enter number of years: "))
if initial_amount < 0 or percentage < 0 or number_of_years <= 0:
    print("invalid input")
invest(initial_amount, percentage, number_of_years)
