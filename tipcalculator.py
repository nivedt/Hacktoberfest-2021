print("Welcome to the tip calculator.")
bill = float(input("What was your total? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = ((tip /100 ) * bill + bill) / people
final_bill = round(bill_with_tip,2)
# print(type(final_bill))

print(f"Each person should pay: ${final_bill}")
