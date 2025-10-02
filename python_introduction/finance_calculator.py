# finance_calculator.py
# Personal Finance Calculator

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print results (formatted to 2 decimal places for currency)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
