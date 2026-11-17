# Get loan details
money_owed = float(input("What is the loan taken, in rupees?"))
apr = float(input("What is annual percentage rate?"))
payment = float(input("How much will you pay every month?"))
months = int(input("How many months do you want to see the results for?"))

#Interest per month
monthly_interest = apr / 100 / 12
print("Monthly interest", monthly_interest * 100, "%")

# Calculate total interest to pay
interest_paid = money_owed*monthly_interest*months
print("Total interest to pay in #", interest_paid, sep="")

# Add in interest
money_owed = money_owed + interest_paid
print("Money owed with interest #", money_owed, sep="")

# Make payment
money_owed = money_owed - payment*months

# Payments
payment = payment*months


# Interest in payments
interest_paid = monthly_interest*months

# Months with monthly_interest
months = months + monthly_interest

# Money paid as interest
interest_money = payment / months


print("Paid #", payment, "of which", interest_paid, "% was interest and money paid as interest is #",interest_money, end="" )
print("Now I owe #", money_owed)