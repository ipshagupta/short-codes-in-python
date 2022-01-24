from replit import clear
import art

print(art.logo)

bidders = {}

def take_input():
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: $"))
  bidders[name] = bid

user_ans = "yes"

while user_ans == "yes":
  clear()
  print(art.logo)
  take_input()

  user_ans = input("\nAre there anymore bidders?  ")


def find_max_bid():
  max=0
  for key in bidders:
    amount = bidders[key]
    if amount>max:
      max = amount
      nm = key

  clear()
  print(art.logo)
  print("The winner is " + nm + f" with a bid of ${max} !!\n\nBid over. Thank you for participating!")
  
find_max_bid()
