# Importing os in order to clear terminal
import art

bids = {}
are_more_people = True
highest_bid = 0
person_with_highest_bid = ""

print(f"""
{art.logo}
Welcome to Silent Auction!
""")

while are_more_people:
    name = input("What is you name?: ")
    person_bid = int(input("What's your bid?: $"))
    bids[name] = person_bid

    if input("Are there more people? ").lower() == "no":
        are_more_people = False

for person in bids:
    if bids[person] > highest_bid:
        highest_bid = bids[person]
        person_with_highest_bid = person

print(f"The person with the highest bid of {highest_bid} is {person_with_highest_bid}")
