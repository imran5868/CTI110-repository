while True:
    num = int(input("Enter an integer: "))
    
    if num < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
    
    repeat = input("Would you like to run the program again? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Exiting program...")
        break
