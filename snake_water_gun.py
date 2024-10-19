import random


def game(computer_choice,user_choice):
    if computer_choice==user_choice:
        return "tie"
    elif (computer_choice=="snake" and user_choice=="water") or (computer_choice=="gun" and user_choice=="snake") or (computer_choice=="water" and user_choice=="gun"):
        return "Computer won"
    else:
        return "You won"
    
choices = ["snake","water","gun"]
#computer choices
computer_choice=random.choice(choices)
#Get user's choice
user_choice=input("Enter you choice from these Snake,Gun,Water: \n").lower()
# count=0
# while True:
#     count=count + 1
#     if count==6:
#         break
#Get valid  choice from user
if user_choice not in choices:
    print("Invalid choice")
#display choices

else:
    print(f"Computer Chose:{computer_choice}")
    print(f"You Chose: {user_choice}")    


#display winner
result=game(computer_choice,user_choice)  
print(result)  

