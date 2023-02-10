import random
import os
print("\n\n\tWelcome to -- ROCK PAPER SSISSORS -- game\n\n")
def rock_paper_scissors():
    n = 1
    computer_score = 0
    user_score = 0
    no_of_plays = int(input("How many times do you want to play?  "))
    while n != no_of_plays+1:
        lst = ["Rock", "Paper", "Scissor"]
        computer = random.choice(lst)
        user_choice = input("Enter your choice: Rock(r), Paper(p), Scissors(s)   : ")
        if computer == "Rock" and user_choice == "s":
            print(f"You: Scissors\nComputer: {computer}\nYou lose this round!!!\n")
            computer_score = computer_score + 1
        elif computer == "Paper" and user_choice == "r":
            print(f"You: Rock\nComputer: {computer}\nYou lose this round!!!\n")
            computer_score = computer_score + 1
        elif computer == "Scissor" and user_choice == "p":
            print(f"You: Paper\nComputer: {computer}\nYou lose this round!!!\n")
            computer_score = computer_score + 1
        elif computer == "Rock" and user_choice == "p":
            print(f"You: Paper\nComputer: {computer}\nYou won this round!!!\n")
            user_score = user_score + 1
        elif computer == "Paper" and user_choice == "s":
            print(f"You: Scissors\nComputer: {computer}\nYou won this round!!!\n")
            user_score = user_score + 1
        elif computer == "Scissor" and user_choice == "r":
            print(f"You: Rock\nComputer: {computer}\nYou won this round!!!\n")
            user_score = user_score + 1
        elif (computer == "Rock" and user_choice == "r") or \
                (computer == "Paper" and user_choice == "p") or\
                (computer == "Scissor" and user_choice == "s"):
            print(f"You: {computer}\nComputer: {computer}\nTied\n")
        else:
            print("Wrong choice entered!!  Try again")
            n = n - 1
        n = n + 1


    print(f"\n\nThe final score is:\nComputer:{computer_score}\nUser:{user_score}")
    if computer_score > user_score:
        print("[ Computer Won ]")
    elif user_score == computer_score:
        print("[ Game tied ]")
    else:
        print("[ You Won ]")

while True:
    rock_paper_scissors()
    choice = input("Do you want to play again: y/n  =")
    if choice == 'y':
        os.system('cls')
        continue
    else:
        exit()