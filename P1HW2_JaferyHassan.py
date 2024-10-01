# Imran Hassan Jafery
# 30 September
# P1HW2_JaferyHassan.
# A brief description of the project

# This program calculates the total travel expenses based on the user's inputs for budget,
# destination, gas, accommodation, and food, and then shows the remaining budget.

# Step 1: Ask the user for their budget
budget = float(input("Enter your budget for the trip: "))

# Step 2: Ask the user for their travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask the user for the amount they will spend on gas
gas_expense = float(input("Enter how much you will spend on gas: "))

# Step 4: Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input("Enter how much you will spend on accommodation: "))

# Step 5: Ask the user for the amount they will spend on food
food_expense = float(input("Enter how much you will spend on food: "))

# Step 6: Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 8: Display the results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_expense:.2f}")
print(f"Accommodation: ${accommodation_expense:.2f}")
print(f"Food: ${food_expense:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
