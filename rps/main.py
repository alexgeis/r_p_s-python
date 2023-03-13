from random import randint


def to_string(hand: str) -> str:
    if hand == "r":
        return "Rock"
    elif hand == "p":
        return "Paper"
    elif hand == "S":
        return "Scissors"
    else:
        return ""


# Read a user input and convert it into r, p, or s.
user_hand: str
u: str = input("Rock (r), Paper (p), or Scissors (s)?").lower()
if u.startswith("r"):
    user_hand = "r"
elif u.startswith("p"):
    user_hand = "p"
elif u.startswith("s"):
    user_hand = "s"
else:
    user_hand = ""

# Randomly pick one of the strings, r, p, and s.
computer_hand: str
randomInt: int = randint(0, 2)
if randomInt == 0:
    computer_hand = "r"
elif randomInt == 1:
    computer_hand = "p"
else:
    computer_hand = "s"

print("You: " + to_string(user_hand) +
      " -- Computer: " + to_string(computer_hand))
