# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the key assumptions
purchase_price = 1000000 # The purchase price of the property
equity_ratio = 0.25 # The equity contribution as a percentage of the purchase price
debt_ratio = 1 - equity_ratio # The debt contribution as a percentage of the purchase price
interest_rate = 0.06 # The interest rate on the debt
loan_term = 10 # The term of the loan in years
amortization_period = 25 # The amortization period in years
annual_growth_rate = 0.02 # The annual growth rate of the property value
annual_rent_growth_rate = 0.02 # The annual growth rate of the rental income
exit_cap_rate = 0.08 # The cap rate at which the property will be sold at the end of the investment horizon
investment_horizon = 5 # The investment horizon in years
equity_IRR_threshold = 0.15 # The minimum required equity IRR

# Calculate the debt and equity amounts
debt_amount = debt_ratio * purchase_price
equity_amount = purchase_price - debt_amount

# Calculate the debt service payments
interest_payment = interest_rate * debt_amount
principal_payment = np.pmt(interest_rate / 12, loan_term * 12, -debt_amount, 0)
debt_service_payment = interest_payment + principal_payment

# Calculate the annual cash flows
annual_rent_income = 50000 # The annual rental income
annual_expenses = 25000 # The annual expenses (e.g., property taxes, maintenance)
annual_debt_service = debt_service_payment * 12 # The annual debt service payment
annual_net_operating_income = annual_rent_income - annual_expenses
annual_cash_flow_before_tax = annual_net_operating_income - annual_debt_service
annual_cash_flow_after_tax = annual_cash_flow_before_tax * 0.8 # Assuming a 20% tax rate

# Calculate the terminal value
terminal_value = annual_cash_flow_before_tax * (1 + annual_rent_growth_rate) / (exit_cap_rate - annual_rent_growth_rate)

# Calculate the equity IRR
cash_flows = [-(equity_amount)] + [annual_cash_flow_after_tax] * investment_horizon + [terminal_value]
equity_irr = np.irr(cash_flows)

# Determine whether the investment meets the minimum equity IRR threshold
if equity_irr >= equity_IRR_threshold:
    print("The investment meets the minimum required equity IRR.")
else:
    print("The investment does not meet the minimum required equity IRR.")