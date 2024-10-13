"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If the user inputs a value that cannot be converted to an integer using int(), a ValueError will be raised.
2. When will a ZeroDivisionError occur?
If the user enters 0 as the denominator, the program will attempt to perform division by zero, which is mathematically undefined and raises a ZeroDivisionError.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, ZeroDivisionError can be prevented by validating the denominator before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero denominator.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
