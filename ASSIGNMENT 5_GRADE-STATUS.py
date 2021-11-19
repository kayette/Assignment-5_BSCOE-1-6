import math

def getEquivalent(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def getGrade():
    inputGrade = float(input("\nEnter your grade percentage: "))
    gradeResult = getEquivalent(inputGrade)
    print("\nYour rounded off input grade is: %.0f" % gradeResult)
    if gradeResult >= 97 and gradeResult <= 100:
        print("Grade Mark: 1.0")
        print("Description: Excellent!\n")
    elif gradeResult >= 94 and gradeResult <= 96:
        print("Grade Mark: 1.25")
        print("Description: Excellent!\n")
    elif gradeResult >= 91 and gradeResult <= 93:
        print("Grade Mark: 1.5")
        print("Description: Very Good!\n")
    elif gradeResult >= 88 and gradeResult <= 90:
        print("Grade Mark: 1.75")
        print("Description: Very Good!\n")
    elif gradeResult >= 85 and gradeResult <= 87:
        print("Grade Mark: 2.0")
        print("Description: Good\n")
    elif gradeResult >= 82 and gradeResult <= 84:
        print("Grade Mark: 2.25")
        print("Description: Good")
    elif gradeResult >= 79 and gradeResult <= 81:
        print("Grade Mark: 2.5")
        print("Description: Satisfactory\n")
    elif gradeResult >= 76 and gradeResult <= 78:
        print("Grade Mark: 2.75")
        print("Description: Satisfactory\n")
    elif gradeResult == 75:
        print("Grade Mark: 3.0")
        print("Description: Passing\n")
    elif gradeResult >= 65 and gradeResult <= 74:
        print("Grade Mark: 5.0")
        print("Description: Failure\n")
    else:
        print("Invalid input. Please check your grade again.\n")

def getStatus():
    statusQ = input("\nEnter your grade status (Inc., W, D): ")
    if (statusQ == "Inc." or "inc"):
        print("\nYour outputs are INCOMPLETE. Please contact your subject teacher.\n")
    elif (statusQ == "W"):
        print("\nYour status in this subject is WITHDRAWN. Please contact your subject teacher if this is a mistake.\n")
    elif (statusQ == "D"):
        print("\nYour status in this subject is DROPPED. Please contact your subject teacher if this is a mistake.\n")
    else:
        print("\nInvalid input. Please try again.\n")

getInput = input('\nGood day!\n \nTo check the equivalent of your grade percentage, type "GRADE".\nTo check your status in the subject, type "STATUS".\n \n= ')
if (getInput == "GRADE"):
    getGrade()
elif (getInput == "STATUS"):
    getStatus()
else: 
    print("\nInvalid input. Please try again.\n")