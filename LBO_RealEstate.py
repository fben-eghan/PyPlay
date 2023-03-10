# Import the required libraries
import numpy as np

# Define the key assumptions
property_value = 10000000 # The value of the commercial property
loan_to_value_ratio = 0.7 # The loan amount as a percentage of the property value
equity_ratio = 1 - loan_to_value_ratio # The equity as a percentage of the property value
interest_rate = 0.05 # The interest rate on the loan
amortization_period = 20 # The amortization period of the loan in years
exit_cap_rate = 0.06 # The cap rate at the end of the investment horizon
investment_horizon = 5 # The investment horizon in years

# Calculate the debt and equity amounts
loan_amount = loan_to_value_ratio * property_value
equity_amount = property_value - loan_amount

# Calculate the debt service payments
interest_payment = interest_rate * loan_amount
principal_payment = np.pmt(interest_rate / 12, amortization_period * 12, -loan_amount, 0)
debt_service_payment = interest_payment + principal_payment

# Calculate the annual net operating income
annual_gross_rental_income = 500000 # The annual gross rental income
annual_operating_expenses = 250000 # The annual operating expenses
annual_net_operating_income = annual_gross_rental_income - annual_operating_expenses

# Calculate the annual cash flows
annual_debt_service = debt_service_payment # The annual debt service payment
annual_cash_flow_before_tax = annual_net_operating_income - annual_debt_service
annual_cash_flow_after_tax = annual_cash_flow_before_tax * 0.8 # Assuming a 20% tax rate

# Calculate the terminal value
terminal_value = annual_cash_flow_before_tax * (1 + exit_cap_rate)**investment_horizon / exit_cap_rate

# Calculate the equity multiple
total_cash_invested = equity_amount
total_cash_proceeds = annual_cash_flow_after_tax * investment_horizon + terminal_value
equity_multiple = total_cash_proceeds / total_cash_invested

# Determine whether the investment meets the minimum required equity multiple
minimum_equity_multiple = 1.5
if equity_multiple >= minimum_equity_multiple:
    print("The investment meets the minimum required equity multiple.")
else:
    print("The investment does not meet the minimum required equity multiple.")
