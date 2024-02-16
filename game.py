import random

def main():
    options = ["stone", "paper", "scissors"]

    while True:
        print("\nWelcome to The Stone, Paper, Scissors Game!!!")
        print("Enter your choice: ")
        print("1. Stone")
        print("2. Paper")
        print("3. Scissors")
        print("4. EXIT THE GAME")

        player_choice = input("Enter your choice (1-4): ")

        if player_choice == "4":
            print("Thanks for playing!")
            break
        elif player_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        player_choice = int(player_choice) - 1
        computer_choice = random.randint(0, 2)

        print("You chose:", options[player_choice])
        print("Computer chose:", options[computer_choice])

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
            print("You win 🏆🏅!")
        else:
            print("Computer wins! 🙁\nBetter luck next time 🤞")

if __name__ == "__main__":
    main()