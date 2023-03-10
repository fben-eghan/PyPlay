# Import the required libraries
import numpy as np

# Define the key assumptions
enterprise_value = 1000000 # The enterprise value of the target company
senior_debt_ratio = 0.6 # The senior debt as a percentage of the enterprise value
junior_debt_ratio = 0.2 # The junior debt as a percentage of the enterprise value
equity_ratio = 1 - senior_debt_ratio - junior_debt_ratio # The equity as a percentage of the enterprise value
senior_interest_rate = 0.05 # The interest rate on the senior debt
senior_amortization_period = 5 # The amortization period of the senior debt in years
junior_interest_rate = 0.10 # The interest rate on the junior debt
junior_amortization_period = 10 # The amortization period of the junior debt in years
exit_multiple = 5 # The exit multiple of the enterprise value at the end of the investment horizon
investment_horizon = 5 # The investment horizon in years
senior_debt_yield_threshold = 0.10 # The minimum required yield on the senior debt

# Calculate the debt and equity amounts
senior_debt_amount = senior_debt_ratio * enterprise_value
junior_debt_amount = junior_debt_ratio * enterprise_value
equity_amount = enterprise_value - senior_debt_amount - junior_debt_amount

# Calculate the senior debt service payments
senior_interest_payment = senior_interest_rate * senior_debt_amount
senior_principal_payment = np.pmt(senior_interest_rate / 12, senior_amortization_period * 12, -senior_debt_amount, 0)
senior_debt_service_payment = senior_interest_payment + senior_principal_payment

# Calculate the junior debt service payments
junior_interest_payment = junior_interest_rate * junior_debt_amount
junior_principal_payment = np.pmt(junior_interest_rate / 12, junior_amortization_period * 12, -junior_debt_amount, 0)
junior_debt_service_payment = junior_interest_payment + junior_principal_payment

# Calculate the annual cash flows
annual_free_cash_flow_to_firm = 100000 # The annual free cash flow to the firm
annual_debt_service = senior_debt_service_payment + junior_debt_service_payment # The annual debt service payment
annual_cash_flow_before_tax = annual_free_cash_flow_to_firm - annual_debt_service
annual_cash_flow_after_tax = annual_cash_flow_before_tax * 0.8 # Assuming a 20% tax rate

# Calculate the terminal value
terminal_value = (annual_cash_flow_before_tax * (1 + 0.03)**investment_horizon) * exit_multiple

# Calculate the senior debt yield
cash_flows = [-(senior_debt_amount)] + [senior_debt_service_payment] * senior_amortization_period + [junior_debt_service_payment] * junior_amortization_period * investment_horizon + [terminal_value]
senior_debt_yield = np.irr(cash_flows)

# Determine whether the investment meets the minimum required senior debt yield
if senior_debt_yield >= senior_debt_yield_threshold:
    print("The investment meets the minimum required senior debt yield.")
else:
    print("The investment does not meet the minimum required senior debt yield.")
