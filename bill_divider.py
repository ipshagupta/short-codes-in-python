print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

tip = float(bill) * (int(percent)/100)
total = float(bill) + tip
each_person = round(total/int(people), 2) 

print(f"Each person should pay: ${each_person}")
