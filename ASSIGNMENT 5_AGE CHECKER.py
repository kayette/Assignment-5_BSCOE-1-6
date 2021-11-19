def ageChecker():
    age = int(input("\nEnter your age: "))
    if age == 1 or age == 8:
        print(f"\nYou're an {age}-year-old Kid. That's so cute!\n")
    elif age >= 0 and age <= 12:
        print(f"\nYou're a {age}-year-old Kid. That's so cute!\n")
    elif age >= 13 and age <= 17:
        print(f"\nYou're a {age}-year-old Teenager. That's so cool!\n")
    elif age == 18:
        print(f"\nYou're a Debutante. Happy first year of legality!\n")
    elif age >= 80 and age <= 89:
        print(f"\nYou're an {age}-year-old Adult. What a grown-up!\n")
    elif age >= 19:
        print(f"\nYou're a {age}-year-old Adult. What a grown-up!\n")
    else:
        print("Invalit input. Please try again.")
        
ageChecker()