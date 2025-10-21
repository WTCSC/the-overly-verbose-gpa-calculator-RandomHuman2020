def bool_parse(instr):
    #this should very much be just *part* of python like it is in C# (Bool.Parse()) but it *isn't*
    return instr.lower() in ("yes", "y", "true", "t", "1")


grade1_input = False
while(not grade1_input):
    grade1 = input("Input your first grade, scale is 0.0 - 4.0 ")
    try:
        grade1 = round(float(grade1), 1)
        if grade1 > 4.0:
            grade1 = 4.0
            print("Your first class' grade has been rounded down to 4.0, as you have input a number higher than 4.0.")
            grade1_input = True
        elif grade1 < 0.0:
            grade1 = 0.0
            print("Your first class' grade has been rounded up to 0.0, as you have input a number lower than 0.0.")
            grade1_input = True
        else:
            grade1 = grade1
            grade1_input = True
    except ValueError:
        print("That's not a number. Try again.")
        grade1_input = False

grade2_input = False
while(not grade2_input):
    grade2 = input("Input your second class' grade, scale is 0.0 - 4.0 ")
    try:
        grade2 = round(float(grade2), 1)
        if grade2 > 4.0:
            grade2 = 4.0
            print("Your second class' grade has been rounded down to 4.0, as you have input a number higher than 4.0.")
            grade2_input = True
        elif grade2 < 0.0:
            grade2 = 0.0
            print("Your second class' grade has been rounded up to 0.0, as you have input a number lower than 0.0.")
            grade2_input = True
        else:
            grade2 = grade2
            grade2_input = True
    except ValueError:
        print("That's not a number. Try again.")
        grade2_input = False

grade3_input = False
while(not grade3_input):
    grade3 = input("Input your third class' grade, scale is 0.0 - 4.0 ")
    try:
        grade3 = round(float(grade3), 1)
        if grade3 > 4.0:
            grade3 = 4.0
            print("Your third class' grade has been rounded down to 4.0, as you have input a number higher than 4.0.")
            grade3_input = True
        elif grade3 < 0.0:
            grade3 = 0.0
            print("Your third class' grade has been rounded up to 0.0, as you have input a number lower than 0.0.")
            grade3_input = True
        else:
            grade3 = grade3
            grade3_input = True
    except ValueError:
        print("That's not a number. Try again.")
        grade3_input = False

grade4_input = False
while(not grade4_input):
    grade4 = input("Input your fourth class' grade, scale is 0.0 - 4.0 ")
    try:
        grade4 = round(float(grade4), 1)
        if grade4 > 4.0:
            grade4 = 4.0
            print("Your fourth class' grade has been rounded down to 4.0, as you have input a number higher than 4.0.")
            grade4_input = True
        elif grade4 < 0.0:
            grade4 = 0.0
            print("Your fourth class' grade has been rounded up to 0.0, as you have input a number lower than 0.0.")
            grade4_input = True
        else:
            grade4 = grade4
            grade4_input = True
    except ValueError:
        print("That's not a number. Try again.")
        grade4_input = False

grade5_input = False
while(not grade5_input):
    grade5 = input("Input your fifth class' grade, scale is 0.0 - 4.0 ")
    try:
        grade5 = round(float(grade5), 1)
        if grade5 > 4.0:
            grade5 = 4.0
            print("Your fifth class' grade has been rounded down to 4.0, as you have input a number higher than 4.0.")
            grade5_input = True
        elif grade5 < 0.0:
            grade5 = 0.0
            print("Your fifth class' grade has been rounded up to 0.0, as you have input a number lower than 0.0.")
            grade5_input = True
        else:
            grade5 = grade5
            grade5_input = True
    except ValueError:
        print("That's not a number. Try again.")
        grade5_input = False

grade6_input = False
while(not grade6_input):
    grade6 = input("Input your sixth class' grade, scale is 0.0 - 4.0 ")
    try:
        grade6 = round(float(grade6), 1)
        if grade6 > 4.0:
            grade6 = 4.0
            print("Your sixth class' grade has been rounded down to 4.0, as you have input a number higher than 4.0.")
            grade6_input = True
        elif grade6 < 0.0:
            grade6 = 0.0
            print("Your sixth class' grade has been rounded up to 0.0, as you have input a number lower than 0.0.")
            grade6_input = True
        else:
            grade6 = grade6
            grade6_input = True
    except ValueError:
        print("That's not a number. Try again.")
        grade6_input = False



grades = [grade1, grade2, grade3, grade4, grade5, grade6]

curr_gpa = round(sum(grades) / len(grades), 2)

#print(grades[0], grades[1], grades[2], grades[3], grades[4])
print(f"Based on the grades you have given for these 6 classes, your GPA is {curr_gpa}.")

analyse_gpa = input("Would you like to split your GPA per semester? ")
if(bool_parse(analyse_gpa)):
    semester = input("Which semester would you like to view the GPA of? ")
    if (int(semester) == 1):
        sem1_grades = grades[:3]
        sem1_gpa = round(sum(sem1_grades) / len(sem1_grades), 2)
        print(f"Your GPA for the first semester is {sem1_gpa}.")
    elif (int(semester) == 2):
        sem2_grades = grades[3:]
        sem2_gpa = round(sum(sem2_grades) / len(sem2_grades), 2)
        print(f"Your GPA for the second semester is {sem2_gpa}.")

makegoal = input("Would you like to make a goal to bring your GPA to? ")
goal_input = False
if(bool_parse(makegoal)):
    while (not goal_input):
        try:
            goal_gpa_userinp = round(float(input("Where would you like to bring your GPA to? (Range from 0.0 to 4.0.) ")), 2)
            if goal_gpa_userinp < 0.0:
                goal_gpa = 0.0
                print("Your goal GPA has been rounded up to 0.0 as you have input a number lower than 0.0.")
                goal_input = True
            elif goal_gpa_userinp > 4.0:
                goal_gpa = 4.0
                print("Your goal GPA has been rounded down to 4.0 as you have input a number higher than 4.0.")
                goal_input = True
            else:
                goal_gpa = goal_gpa_userinp
                goal_input = True


        except ValueError:
            print("That's not a valid GPA!")
            goal_input = False
    if goal_gpa < curr_gpa:
        print("You appear to have already met or exceeded your goal GPA. Congrats!")
        quit()
    else:
        found = False
        tempgrades = [grade1, grade2, grade3, grade4, grade5, grade6]
        currentgrade = 0
        while found is False and currentgrade < 6:
            tempgrades[currentgrade] = 4
            currentgrade += 1
            temp_gpa = sum(tempgrades) / len(tempgrades)
            if temp_gpa >= goal_gpa:
                found = True
                print(f"You can increase your GPA to meet your goal of {goal_gpa} by increasing the grade of class #{currentgrade} to 4.0.")
            else:
                found = False
                tempgrades = [grade1, grade2, grade3, grade4, grade5, grade6]
        if not found:
            print(
                "Looks like you'll need to increase the grades of multiple classes to reach your goal. Sorry, but I can't calculate the required increase for more than one class.")

