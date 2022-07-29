import art
import random
from gamedata import data


def print_info(index_in_data):
    """Return the name, desc and country of a person based on index given."""
    return f'{data[index_in_data]["name"]}, a {data[index_in_data]["description"]}, from {data[index_in_data]["country"]}'


def pick_winner(indexA, indexB):
    """Picks the winner using the index given while looking at gamedata.py."""
    if data[indexA]["follower_count"] > data[indexB]["follower_count"]:
        return "A"
    else:
        return "B"


personAindex = random.randint(0, len(data))
score = 0


def game():
    global personAindex
    global score
    personBindex = random.randint(0, len(data))
    print(f"""
    {art.higher_lower}
    Compare A: {print_info(personAindex)}
    {art.vs}
    Against B: {print_info(personBindex)}
    """)
    if input("Who has more followers? Type 'A' or 'B': ").upper() == pick_winner(personAindex, personBindex):
        personAindex = personBindex
        score += 1
        print(f"Good Job! Current Score: {score}")
        game()
    else:
        print(f"You lost! Max Score: {score}")


game()
