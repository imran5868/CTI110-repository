# Imran Hassan Jafrey 
# 11/10/24
# P4HW2
# This program calculates the gross pay for multiple employees, including overtime, and displays totals for all employees.
# Initialize accumulators for totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0
# Loop to process multiple employees
while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    # Check for sentinel value to end the program
    if employee_name.lower() == "done":
        break
    # Get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    # Calculate overtime and regular pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        overtime_hours = 0
        regular_hours = hours_worked
        overtime_pay = 0
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
    
    # Display employee's pay information
    print("\nEmployee name: ", employee_name)
    print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<10}")
    print("-" * 60)
    print(f"{hours_worked:<15.2f} {pay_rate:<10.2f} {overtime_hours:<10.2f} {overtime_pay:<15.2f} {regular_pay:<15.2f} {gross_pay:<10.2f}")
    print()  
    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1
# Display summary of totals
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
