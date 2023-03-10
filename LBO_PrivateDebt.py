class PrivateDebt:
    def __init__(self, principal, interest_rate, loan_term, monthly_payment):
        self.principal = principal # Step 1: Initialize the input variables as instance attributes
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.monthly_payment = monthly_payment

    def total_interest_paid(self):
        monthly_rate = self.interest_rate / 12 # Step 2: Calculate monthly interest rate
        num_payments = self.loan_term * 12 # Step 3: Calculate total number of loan payments
        total_paid = self.monthly_payment * num_payments # Step 4: Calculate total amount paid over the loan term
        total_interest = total_paid - self.principal # Step 5: Calculate total interest paid
        return total_interest

    def remaining_balance(self, n_months):
        monthly_rate = self.interest_rate / 12 # Step 6: Calculate monthly interest rate
        num_payments = self.loan_term * 12 # Step 7: Calculate total number of loan payments
        remaining_principal = self.principal * ((1 + monthly_rate) ** num_payments - (1 + monthly_rate) ** n_months) / ((1 + monthly_rate) ** num_payments - 1) # Step 8: Calculate remaining principal after n_months
        return remaining_principal

# Example usage
loan1 = PrivateDebt(100000, 0.06, 5, 1933.21) # Step 9: Create an instance of PrivateDebt class with input variables
print("Total Interest Paid: $", round(loan1.total_interest_paid(), 2)) # Step 10: Call total_interest_paid method, round to 2 decimal places, and print result
print("Remaining Balance after 24 Months: $", round(loan1.remaining_balance(24), 2)) # Step 11: Call remaining_balance method with n_months = 24, round to 2 decimal places, and print result
