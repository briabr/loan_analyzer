# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]
num_loans = len(loan_costs)
print(f"the number of loans is {num_loans}")

total_loans = sum(loan_costs)
print(f"The total loans is {total_loans}")

avg_loan_price = total_loans/num_loans
print(f"The average loan price is {avg_loan_price}")