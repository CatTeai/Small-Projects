# We're going to create a chore list decider. it will ask the user for a list of up to 5 of their chores, and the computer will select a random one for the user to do. 
# once the option has been selected, it will be deleted from the list and the prompt will run again but with the previously selected choice removed from the list, 
# until all chores are selected. after list is empty, program will congratulate user on doing all of their tasks. yahoo!

#adding neccesary import to enable random choices 
import random

# first step: ask user to input 5 chores they need done
chore_list = []
for i in range(5):
    chore_list.append((input("Enter the chore you need to do! ")))

# second step: confirming list is accurate
choice_list1 = ['Y', 'N']
userchoice_1 = input('Are you happy with this list? Y/N ')

if userchoice_1 == 'Y':
    print("Great! Let's decide what task you'll do.")

if userchoice_1 == 'N': 
    print("Rerun the program then. Loser.")

# third step: have computer decide chore for user
computer_choice = random.choice(chore_list)
computer_choice2 = random.choice(chore_list)
print('Do this task first:', computer_choice)
print('After that task, do this one next:', computer_choice2)
print("Don't like my answer? Too bad, you decided to ask a computer for an opinion and this is it. Maybe try deciding on your own next time if you're gonna be picky.")
