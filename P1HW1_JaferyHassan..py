Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Imran Hassan Jafery
... # 30 September
... # P1HW1_JaferyHassan.
... 
... # This program performs two tasks: 
... # 1. It calculates the exponentiation of a base number raised to a power.
... # 2. It performs addition and subtraction based on user inputs.
... 
... # Part 1: Calculating Exponents
... print("-----Calculating Exponents----")
... base = int(input("Enter an integer as the base value: "))
... exponent = int(input("Enter an integer as the exponent: "))
... result = base ** exponent
... print(f"\n{base} raised to the power of {exponent} is {result} !!\n")
... 
... # Part 2: Addition and Subtraction
... print("-----Addition and Subtraction----")
... start_value = int(input("Enter a starting integer: "))
... add_value = int(input("Enter an integer to add: "))
... subtract_value = int(input("Enter an integer to subtract: "))
... final_result = start_value + add_value - subtract_value
... print(f"\n{start_value} + {add_value} - {subtract_value} is equal to {final_result}")
