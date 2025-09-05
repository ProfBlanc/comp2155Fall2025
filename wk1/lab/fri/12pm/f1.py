answer = input("Enter a grade: ")

try:
    grade = int(answer)
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")
    print("Your grade is ", grade)
except ValueError as e:
    print("Invalid input: ", e)
