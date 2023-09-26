import random

user_score = 0
computer_score = 0

print('ROCK PAPER SCISSORS\n')
     
while True:
    print("1.Rock 2.Paper 3.Scissors")

    # Take the input from the user
    choice = int(input("Enter your choice: "))

    # Check for valid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice (1, 2, or 3): '))

    # Define the choices
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

    # Get the user's choice name
    choice_name = choices[choice]

    # Print user choice
    print('User choice is:', choice_name)

    # Computer chooses randomly among 1, 2, and 3 using randint method of the random module
    comp_choice = random.randint(1, 3)

    # Ensure that the computer's choice is different from the user's choice
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # Get the computer's choice name
    comp_choice_name = choices[comp_choice]

    print("Computer choice is:", comp_choice_name)

    # Determine the winner
    if (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
        result = 'User'
    elif (comp_choice == 1 and choice == 3) or (comp_choice == 2 and choice == 1) or (comp_choice == 3 and choice == 2):
        result = 'Computer'
    else:
        result = 'Draw'

    # Print the result
    if result == 'Draw':
        print("It's a Draw!")
    else:
        print(f"{result} wins!")

    # Update the scores
    if result == 'User':
        user_score += 1
    elif result == 'Computer':
        computer_score += 1

    print(f"User Score: {user_score}, Computer Score: {computer_score}")

    play_again = input("Do you want to play again? (Y/N): ").strip().lower()
    print('\n')

    if play_again != 'y':
        break

# After coming out of the loop, print thanks for playing
print("Thanks for playing\n")
