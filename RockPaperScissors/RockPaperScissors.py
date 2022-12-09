#Mathew, Josh S2201761
import random
import time


print("Pick Rock, Paper or Scissors!")
UserPick = input()

R = "rock"
P = "paper"
S = "scissors"

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''
paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''
scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

rockComp =   '''
   _______    
  (____   '---
 (_____)      
 (_____)      
  (____)      
   (___)__.---
           '''
paperComp = '''
      _______    
 ____(____   '---
(______          
(_______          
(_______        
     (__________.---
                 '''
scissorComp='''  
        _______    
   ____(____   '---
  (______          
  (__________      
      (____)      
        (___)__.---
 '''

Computer = ["rock","paper","scissors"]
compPick =  random.choice(Computer)

if UserPick.upper() == compPick[0].upper():
    print("Game result:")
    time.sleep(4)
    print("It's a TIE!!")

elif UserPick.upper() == "R" or "Rock":
    if compPick == "scissors":
    #or "S":
        print(f"Congratulations, you won. {rock} VS {scissorComp}")
    else:
        print(f"Unfortunately, you lost mate. {rock} VS {paperComp}")

elif UserPick.upper() == "P" or "Paper":
    if compPick == "rock":
   # or "R":
        print(f"Congratulations, you won. {paper} VS {rockComp}")
    else:
        print(f"Unfortunately, you lost mate. {paper} VS {scissorComp}")

elif UserPick.upper() == "S" or "Scissors":
    if compPick == "paper":
    # or "P":
        print(f"Congratulations, you won. {scissors} VS {paperComp}")
    else:
        print(f"Unfortunately, you lost mate. {scissors} VS {rockComp}")