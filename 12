def play_game():
    while True:
        player1 = input("Player 1, enter Rock/Paper/Scissors: ").lower()
        player2 = input("Player 2, enter Rock/Paper/Scissors: ").lower()

        if player1 == player2:
            print("It's a tie!")
        elif (player1 == "rock" and player2 == "scissors") or \
             (player1 == "scissors" and player2 == "paper") or \
             (player1 == "paper" and player2 == "rock"):
            print("Player 1 wins! 🎉")
        else:
            print("Player 2 wins! 🎉")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            break

play_game()
