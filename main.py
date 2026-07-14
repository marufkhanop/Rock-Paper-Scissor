import random as rn
import sys
choice = ["r", "p", "s"]
while True:
  user = input("Enter your choice(r, p, s): ")
  if user in choice:
    bot = rn.choice(choice)
    print(f"I choose '{bot}'")
    if user == bot:
      sys.exit("TIE")
    elif (bot, user) in (("r","s"),("p","r"),("s","p")):
      sys.exit("Computer Wins")
    else:
      sys.exit("You Win")
