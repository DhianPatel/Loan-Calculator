import streamlit as st


# Get loan details
money_owed = float(st.text_input("What is the loan taken, in rupees?"))
apr = float(st.text_input("What is annual percentage rate?"))
payment = float(st.text_input("How much will you pay every month?"))
months = int(st.text_input("How many months do you want to see the results for?"))

#Interest per month
monthly_interest = apr / 100 / 12
st.write("Monthly interest", monthly_interest * 100, "%")

# Calculate total interest to pay
interest_paid = money_owed*monthly_interest*months
st.write("Total interest to pay in #", interest_paid, sep="")

# Add in interest
money_owed = money_owed + interest_paid
st.write("Money owed with interest #", money_owed, sep="")

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


st.write("Paid #", payment, "of which", interest_paid, "% was interest and money paid as interest is #",interest_money, end="" )
st.write("Now I owe #", money_owed)