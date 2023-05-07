# We're going to create a chore list decider. it will ask the user for a list of up to 5 of their chores, and the computer will select a random one for the user to do. 
# once the option has been selected, it will be deleted from the list and the prompt will run again but with the previously selected choice removed from the list, 
# until all chores are selected. after list is empty, program will congratulate user on doing all of their tasks. yahoo!

#adding neccesary import to enable random choices 
import random
from random import randrange

# first step: ask user to input 5 chores they need done
chore_list = []
for i in range(5):
    chore_list.append((input("Enter the chore you need to do! ")))

# second step: confirming list is accurate
choice_list1 = ['Y', 'N']
userchoice_1 = input('Are you happy with this list? Y/N ')

if userchoice_1 == 'Y':
    print("Great! Let's decide what task you'll do.")
    print(" ")

if userchoice_1 == 'N': 
    print("Rerun the program then. Loser.")

# third step: have computer decide chore for user

computer_choice = chore_list.pop(randrange(len(chore_list)))
computer_choice2 = chore_list.pop(randrange(len(chore_list)))
computer_choice3 = chore_list.pop(randrange(len(chore_list)))
computer_choice4 = chore_list.pop(randrange(len(chore_list)))
computer_choice5 = chore_list.pop(randrange(len(chore_list)))

choice_list2 = ['yes', 'no']

print("Let's do this task first:", computer_choice) 
print(" ")
print("Let me know when you're all finished.")
print(" ")
user_choice2 = input("Have you finished? If you are, type yes: ")

if user_choice2 == 'no':
 print("Then get to it! I didn't say tell me no, I said to tell me when you're done. Smartass. Have you actually finished this time?")

if user_choice2 == 'yes':
 print('Great job! The first task is always the hardest. Do this one next:', computer_choice2)
 print(" ")
 
user_choice3 = input( "Have you finished? Type yes if so:")

if user_choice3 == 'no':
 print("Then get to it! I didn't say tell me no, I said to tell me when you're done. Smartass. Have you actually finished this time?")

if user_choice3 == 'yes':
 print('Amazing! Only a few more to go. How about we do this one:', computer_choice3)
 print(" ")
 
user_choice4 = input("When you're all done, type yes :) :")

if user_choice4 == 'no':
 print("Then get to it! I didn't say tell me no, I said to tell me when you're done. Smartass. Have you actually finished this time?")

if user_choice4 == 'yes':
 print("Awesome! Good going. You're almost done, let's keep pushing. For your next one, do this:", computer_choice4)
 print(" ")
 
user_choice5 = input("Are you all done that task? Let me know! :")

if user_choice5 == 'no':
 print("Then get to it! I didn't say tell me no, I said to tell me when you're done. Smartass. Have you actually finished this time?")

if user_choice5 == 'yes':
    print("I'm so proud of you! Just one more task left. All you need to do is", computer_choice5)
    print(" ")
    
user_choice6 = input("Are you all done? :")

if user_choice6 == 'no':
 print("Then get to it! I didn't say tell me no, I said to tell me when you're done. Smartass. Have you actually finished this time?")

if user_choice6 == 'yes':
    print(" ")
    print("WOOHOO!! Congratulations, everything you need to do has been done. You're such a hard worker, go enjoy yourself. :3")
    print("Have a great day , stay hydrated, and keep being you!")
    print(" ")

#End of code