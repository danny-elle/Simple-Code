def compare(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    elif grade2 >= 50:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)

#the correct format to decide whether a grade is passing
#and to get the average of the passing grade(s)
def compare1(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    if grade2 >= 50:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)


def cmp2(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    else:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)


def cmp3(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50 and grade2 >= 50:
        total = grade1 + grade2
        grade_count = 2

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)
