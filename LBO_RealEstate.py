class LBO_RE:
    def __init__(self, purchase_price, down_payment, closing_costs, interest_rate, loan_term, rental_income, expenses):
        self.purchase_price = purchase_price # Step 1: Initialize the input variables as instance attributes
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.rental_income = rental_income
        self.expenses = expenses

    def loan_amount(self):
        return self.purchase_price - self.down_payment # Step 2: Calculate the loan amount using input variables

    def monthly_mortgage_payment(self):
        loan_amount = self.loan_amount() # Step 3: Call loan_amount method to get loan amount
        monthly_rate = self.interest_rate / 12 # Step 4: Calculate monthly interest rate
        num_payments = self.loan_term * 12 # Step 5: Calculate total number of mortgage payments
        mortgage_payment = loan_amount * monthly_rate * (1 + monthly_rate) ** num_payments / ((1 + monthly_rate) ** num_payments - 1) # Step 6: Calculate monthly mortgage payment
        return mortgage_payment

    def net_operating_income(self):
        return self.rental_income - self.expenses # Step 7: Calculate net operating income

    def cash_flow_before_taxes(self):
        mortgage_payment = self.monthly_mortgage_payment() # Step 8: Call monthly_mortgage_payment method to get monthly mortgage payment
        NOI = self.net_operating_income() # Step 9: Call net_operating_income method to get net operating income
        CFBT = NOI - mortgage_payment # Step 10: Calculate cash flow before taxes
        return CFBT

    def cash_on_cash_return(self):
        CFBT = self.cash_flow_before_taxes() # Step 11: Call cash_flow_before_taxes method to get cash flow before taxes
        total_cash_invested = self.down_payment + self.closing_costs # Step 12: Calculate total cash invested
        annual_CFBT = CFBT * 12 # Step 13: Calculate annual cash flow before taxes
        CoC = annual_CFBT / total_cash_invested # Step 14: Calculate cash-on-cash return
        return CoC

# Example usage
property1 = LBO_RE(1000000, 200000, 5000, 0.05, 10, 8000, 2000) # Step 15: Create an instance of LBO class with input variables
print("Loan Amount: $", property1.loan_amount()) # Step 16: Call loan_amount method and print result
print("Monthly Mortgage Payment: $", property1.monthly_mortgage_payment()) # Step 17: Call monthly_mortgage_payment method and print result
print("Net Operating Income (NOI): $", property1.net_operating_income()) # Step 18: Call net_operating_income method and print result
print("Cash Flow Before Taxes (CFBT): $", property1.cash_flow_before_taxes()) # Step 19: Call cash_flow_before_taxes method and print result
print("Cash-on-Cash Return (CoC):", round(property1.cash_on_cash_return() * 100, 2), "%") # Step 20: Call cash_on_cash_return method, multiply by 100, round to 2 decimal places, and print result
