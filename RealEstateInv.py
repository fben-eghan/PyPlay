import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class RealEstateInvestment:
    def __init__(self, purchase_price=1000000, equity_ratio=0.25, interest_rate=0.06, loan_term=10, 
                 amortization_period=25, annual_growth_rate=0.02, annual_rent_growth_rate=0.02, 
                 exit_cap_rate=0.08, investment_horizon=5, equity_IRR_threshold=0.15,
                 annual_rent_income=50000, annual_expenses=25000, tax_rate=0.2):
        
        self.purchase_price = purchase_price  # property purchase price
        self.equity_ratio = equity_ratio  # proportion of purchase price paid with equity
        self.debt_ratio = 1 - equity_ratio  # proportion of purchase price financed with debt
        self.interest_rate = interest_rate  # annual interest rate on the loan
        self.loan_term = loan_term  # term of the loan in years
        self.amortization_period = amortization_period  # period over which the loan is amortized
        self.annual_growth_rate = annual_growth_rate  # annual growth rate of the property value
        self.annual_rent_growth_rate = annual_rent_growth_rate  # annual growth rate of the rental income
        self.exit_cap_rate = exit_cap_rate  # capitalization rate at which the property is sold
        self.investment_horizon = investment_horizon  # investment horizon in years
        self.equity_IRR_threshold = equity_IRR_threshold  # minimum required equity IRR
        self.annual_rent_income = annual_rent_income  # annual rental income
        self.annual_expenses = annual_expenses  # annual property expenses
        self.tax_rate = tax_rate  # marginal tax rate of the investor

    def calculate(self):
        try:
            # Calculate the debt and equity amounts
            debt_amount = self.debt_ratio * self.purchase_price
            equity_amount = self.purchase_price - debt_amount

            # Calculate the debt service payments
            interest_payment = self.interest_rate * debt_amount
            principal_payment = np.pmt(self.interest_rate / 12, self.loan_term * 12, -debt_amount, 0)
            debt_service_payment = interest_payment + principal_payment

            # Calculate the annual cash flows
            annual_debt_service = debt_service_payment * 12
            annual_net_operating_income = self.annual_rent_income - self.annual_expenses
            annual_cash_flow_before_tax = annual_net_operating_income - annual_debt_service
            annual_cash_flow_after_tax = annual_cash_flow_before_tax * (1 - self.tax_rate)
            
            # Calculate the terminal value
            terminal_value = annual_cash_flow_before_tax * (1 + self.annual_rent_growth_rate) / (self.exit_cap_rate - self.annual_rent_growth_rate)

            # Calculate the equity IRR
            cash_flows = [-(equity_amount)] + [annual_cash_flow_after_tax] * self.investment_horizon + [terminal_value]
            equity_irr = np.irr(cash_flows)

            # Determine whether the investment meets the minimum equity IRR threshold
            if equity_irr >= self.equity_IRR_threshold:
                print("The investment meets the minimum required equity IRR.")
            else:
                print("The investment does not meet the minimum required equity IRR.")
               
              
# Create an instance of the RealEstateInvestment class
rei = RealEstateInvestment()

# Call the calculate method to perform the calculations and print the result
rei.calculate()

# Create two instances of the RealEstateInvestment class with different input parameters
rei1 = RealEstateInvestment(purchase_price=800000, annual_rent_income=45000, annual_expenses=20000)
rei2 = RealEstateInvestment(purchase_price=1200000, annual_rent_income=60000, annual_expenses=30000)

# Call the calculate method for each object to perform the analysis and print the results
print("Scenario 1:")
rei1.calculate()
print("\nScenario 2:")
rei2.calculate()

# Create a list of investment objects and loop through them to create graphs
investments = [rei1, rei2]
for i, investment in enumerate(investments):
    # Create a list of years
    years = [x for x in range(1, investment.investment_horizon + 2)]

    # Create a list of annual cash flows
    cash_flows = [-investment.equity_amount] + [investment.annual_cash_flow_after_tax] * investment.investment_horizon + [investment.terminal_value]

    # Create a bar plot of annual cash flows
    plt.subplot(2, 2, i + 1)
    plt.bar(years, cash_flows)
    plt.title(f"Scenario {i + 1}: Annual Cash Flows")
    plt.xlabel("Year")
    plt.ylabel("Cash Flow")

    # Create a line plot of cumulative cash flows
    cumulative_cash_flows = np.cumsum(cash_flows)
    plt.subplot(2, 2, i + 3)
    plt.plot(years, cumulative_cash_flows)
    plt.title(f"Scenario {i + 1}: Cumulative Cash Flows")
    plt.xlabel("Year")
    plt.ylabel("Cumulative Cash Flow")

# Adjust the layout and display the plots
plt.tight_layout()
plt.show()
