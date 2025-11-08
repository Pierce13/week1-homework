# Monthly Savings Calculator

# Ask for user inputs
name = input("Enter your name: ")
income = float(input("Enter your monthly income: "))
rent = float(input("Enter your rent/mortgage: "))
food = float(input("Enter your food expenses: "))
transport = float(input("Enter your transportation costs: "))

# Calculate total expenses and savings
total_expenses = rent + food + transport
savings = income - total_expenses

# Calculate percentage of income saved
if income > 0:
    percent_saved = (savings / income) * 100
else:
    percent_saved = 0

# Display results in matching format
print(f"\n--- Monthly Budget Summary for {name} ---")
print(f"Total monthly expenses: ${total_expenses:,.2f}")
print(f"Remaining savings: ${savings:,.2f}")
print(f"Percentage of income saved: {percent_saved:.1f}%")
