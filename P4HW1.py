# Imran Hassan Jafrey 
# 11/10/24
#  P4HW1
# This program collects scores from the user, validates them, calculates average, and determines a letter grade.
# Step 1: Ask the user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))
scores = []

# Step 2: Collect scores with validation
for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i} again:")

# Step 3: Calculate results
lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average_score = sum(modified_scores) / len(modified_scores)

# Determine letter grade based on average
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Step 4: Display results
print("\n--------------Results--------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {modified_scores}")
print(f"Scores Average : {average_score:.2f}")
print(f"Grade          : {grade}")
print("-----------------------------------")
