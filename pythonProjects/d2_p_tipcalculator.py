# if the bill was $150.00 , split between 5 peoples , with 12% tip.not
# Each person should pay (150 / 5) * 1.12 = 33.6
# round the result to 2 decimal places = 33.60
print("welcome to tip calculator_project!")
bill = float(input("what was the total bill$ "))
tip = int(input("how much tip would you like to give? 10 or 20? "))
people = int(input("how many people to split the bill? "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
# final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")