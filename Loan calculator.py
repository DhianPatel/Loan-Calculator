import streamlit as st

# Sets the browser tab title and calculator icon
st.set_page_config(page_title="Loan Calculator", page_icon="🧮")

st.title("🧮 Loan Calculator")

# Get loan details
money_owed = st.number_input("What is the loan taken, in rupees (₹)?", min_value=0.0)
apr = st.number_input("What is annual percentage rate (%)", min_value=0.0)
payment = st.number_input("How much will you pay every month (₹)?", min_value=0.0)
months = st.number_input("How many months do you want to see the results for?", min_value=1, step=1)

# Interest per month
monthly_interest = apr / 100 / 12
st.write(f"📊 Monthly interest: {monthly_interest * 100:.2f}%")

# Calculate total interest to pay
interest_paid = money_owed * monthly_interest * months
st.write(f"💸 Total interest to pay: ₹{interest_paid:,.2f}")

# Add in interest
money_owed = money_owed + interest_paid
st.write(f"💰 Money owed with interest: ₹{money_owed:,.2f}")

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

st.write(f"✅ Paid ₹{payment:,.2f} of which {interest_paid:.2f}% was interest and money paid as interest is ₹{interest_money:,.2f}")
st.write(f"🏦 Now I owe: ₹{money_owed:,.2f}")
