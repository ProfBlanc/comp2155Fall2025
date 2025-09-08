"""
Ask the user for a grade. Ensure grade is between 0-100
"""
# import sys
answer = input("Enter a grade: ")
try:
    grade = int(answer)
    if grade < 0 or grade > 100:
        raise ValueError("Incorrect Grade")
    print("Your grade is", grade)
except ValueError as e:
    #    print(e, file=sys.stderr)
    print(e)

