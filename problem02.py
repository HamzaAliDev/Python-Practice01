# Leap Year Check:
# Write a Python function that checks if a given year is a leap year. 
# A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

year = int(input("Enter full year: "))
if year%4 == 0:
    print("Its a leap year")
else:
    print("Its not a leap year")