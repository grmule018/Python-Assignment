amount = int(input("Enter the amount: "))
interest = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))
for x in range(1, years+1):
    amount = (amount*((100+interest)/100))
print(amount)
