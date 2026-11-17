import streamlit as st

st.set_page_config(
    page_title="Dhian's Weather Forecast App",
)

st.write(
    f"Calculate the loan you have taken.")

# Get loan details using number_input so empty boxes don't crash the app
money_owed = st.number_input("What is the loan taken, in rupees?", min_value=0.0)
apr = st.number_input("What is annual percentage rate?", min_value=0.0)
payment = st.number_input("How much will you pay every month?", min_value=0.0)
months = st.number_input(
    "How many months do you want to see the results for?", min_value=1, step=1
)

# Interest per month
monthly_interest = apr / 100 / 12
st.write(f"Monthly interest: {monthly_interest * 100}%")

# Calculate total interest to pay
interest_paid = money_owed * monthly_interest * months
st.write(f"Total interest to pay in #{interest_paid}")

# Add in interest
money_owed = money_owed + interest_paid
st.write(f"Money owed with interest #{money_owed}")

# Make payment
money_owed = money_owed - payment * months

# Payments
payment = payment * months

# Interest in payments
interest_paid = monthly_interest * months

# Months with monthly_interest
months = months + monthly_interest

# Money paid as interest
interest_money = payment / months

st.write(
    f"Paid #{payment} of which {interest_paid}% was interest and money paid as"
    f" interest is #{interest_money}"
)
st.write(f"Now I owe #{money_owed}")
