"""
**Driving License Eligibility** - Age ≥ 18: Ask if test passed (yes/no). - Yes: "License Approved" | No: "Test not cleared." - Age < 18: "Not eligible due to age."
"""
age = int(input("Enter your age: "))

if age >= 18:
    test = input("Have you passed the driving test? (yes/no): ")

    if test == "yes":
        print("License Approved")
    else:
        print("Test not cleared.")
else:
    print("Not eligible due to age.")

    
