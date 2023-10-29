print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip_input = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_modifier = (tip_input / 100) + 1
person_total = int(input("How many people to split the bill? "))

shared_bill = (bill * tip_modifier) / person_total

#Within the f-string variable, we can add :.2f to show 2 decimal places, 3, etc.
print(f"Each person should pay: ${shared_bill:.2f}")