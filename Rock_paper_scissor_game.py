import random


options = ['rock', 'paper', 'scissor']


def check_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def start_match(player_name):
    player_points = 0
    cpu_points = 0
    round_log = []
    round_id = 1

    print(f"\nWelcome {player_name}! First to 2 wins. Let's begin:\n")

    while player_points < 2 and cpu_points < 2:
        print(f"Round {round_id}")
        player_move = input("Choose (rock/paper/scissor): ").strip().lower()

        if player_move not in options:
            print(" Invalid choice. Try again!\n")
            continue

        cpu_move = random.choice(options)
        print(f"You picked: {player_move}")
        print(f"Computer picked: {cpu_move}")

        outcome = check_winner(player_move, cpu_move)

        if outcome == "tie":
            print(" It's a tie!\n")
            round_log.append((round_id, player_move, cpu_move, "Tie"))
        elif outcome == "player":
            print("You win this round!\n")
            player_points += 1
            round_log.append((round_id, player_move, cpu_move, "Player Wins"))
        else:
            print("💻 Computer wins this round!\n")
            cpu_points += 1
            round_log.append((round_id, player_move, cpu_move, "Computer Wins"))

        round_id += 1

    # Match end summary
    print("\n🏁 Match Finished!")
    print(f"Final Score => {player_name}: {player_points} | Computer: {cpu_points}")
    winner = player_name if player_points > cpu_points else "Computer"
    print(f" Winner: {winner}\n")

    print(" Round History:")
    for log in round_log:
        print(f"Round {log[0]}: You={log[1]}, Computer={log[2]} → {log[3]}")

# Main game loop
def run_game():
    print("🎮 Let's play Rock, Paper, Scissors!")
    name = input("Enter your name: ").strip()

    while True:
        start_match(name)
        replay = input("\nPlay again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print(" Thanks for playing. Goodbye!")
            break

# Start the game
run_game()
