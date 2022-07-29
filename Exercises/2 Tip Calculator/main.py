print("Welcome to the Tip calculator. Made by Arben KRYEMADHI!")
bill = float(input("What was teh totall bill? $"))
tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12, 15? "))
persons = int(input("How many people are splitting the bill? "))

calculated_tip = 1 + tip_percentage / 100

payment_per_person = "{:.2f}".format(round(bill * calculated_tip / persons))
print(f"Each person should pay ${payment_per_person}")
