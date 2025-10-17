grade1_input = False
while(not grade1_input):
    grade1 = input("input your first grade, scale is 0.0 - 4.0")
    try:
        grade1 = round(float(grade1), 1)
        if grade1 < 4.0:
            grade1 = 4.0
            print("Your first class' grade has been rounded down to 4.0, as you have inputted a number higher than 4.0.")
            grade1_input = True
        elif grade1 > 0.0:
            grade1 = 0.0
            print("Your first class' grade has been rounded down to 0.0, as you have inputted a number lower than 0.0.")
            grade1_input = True
        else:
            grade1 = grade1
            grade1_input = False
    except ValueError:
        print("That's not a number. Try again.")




grade2 = input("input your second grade, scale is 0.0 - 4.0")
grade3 = input("input your third grade, scale is 0.0 - 4.0")
grade4 = input("input your fourth grade, scale is 0.0 - 4.0")
grade5 = input("input your fifth grade, scale is 0.0 - 4.0")

grades = [grade1, grade2, grade3, grade4, grade5, grade6]


print(grades[0], grades[1], grades[2], grades[3], grades[4])