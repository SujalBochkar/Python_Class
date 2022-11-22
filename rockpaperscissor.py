# Rock Paper Scissor

import random
print("Welcome to the game")
uc = input("Enter either rock or paper or scissor\n")
cc = ["rock", "paper", "scissor"]
cs = random.choice(cc)
print(f"User Choice is {uc} \nComputer Choice is {cs} \n")

if uc == cs:
    print("Its a Tie")
elif uc == "rock" and cs == "paper": 
    print("Computer is won")
elif uc == "paper" and cs == "scissor" :
    print("Computer is won")
elif uc == "scissor" and cs== "rock" :
    print("Computer is won")
elif uc == "paper" and cs == "rock" :
    print("User is won")
elif uc == "scissor" and cs == "paper" :
    print("User is won")
elif uc == "rock" and cs == "scissor" :
    print("User is won")
else:
    print("Not valid")
