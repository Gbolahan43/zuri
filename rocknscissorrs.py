import random
while True :

    print("make your Throw")
    user_choice = input("Enter your choice (rock, paper, scissors) : ")
    possible_outcome = ["rock", "scissors", "paper"]
    computer_choice = random.choice(possible_outcome)

    while user_choice not in possible_outcome:
        user_choice = input("Enter your choice (rock, paper, scissors) : ").lower()

    if user_choice == computer_choice:
        print(f"Bot players selected {user_choice}. It's a tie !")
    elif user_choice == "rock" :
        if computer_choice == "scissors" :
             print("Rock smashes  scissors. you win !")
        else:
            print("Paper covers rock!. You lose")
    elif user_choice == "paper" :
        if computer_choice == "rock":
            print("Paper covers rock!. You win!")
        else:
            print("Scissors cuts paper!. You lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper!. You win!")
        else:
            print('rock smashes scissors!. You lose. ')
    
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("GoodBye")
