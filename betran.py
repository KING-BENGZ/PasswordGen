import random

#Id first take in the valid inputs i need 
print("What is your name ?")
name = str(input())
print("What is your age?")
age = int(input())
print("What is your dogs name  ?")
dogName = str(input())
# Then i manipulate the strings with a bunch of for loops 
passwords = [f"{name}{age}{dogName}{each}{a}" for each in ["A","B","C","D"]  for a in range(7) ]
print ("These are weak passwords :", passwords)
# I then add special characters to the mix 
strongPassword = [f'{a}{b}{name}{c}{d}' for a in ["A","B","C","D"] for b in ["O", "Q" , "Z", "X"] for c in range(3) for d in {".",",","!","/"}]
print ("These are stronger passwords : " , strongPassword)
