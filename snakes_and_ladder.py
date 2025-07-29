import random


FINAL_POSITION = 100


snakes = {
    99: 7,
    92: 35,
    89: 70,
    74: 53,
    62: 19,
    64: 60,
    46: 15,
    49: 11,
    16: 6
}

ladders = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94
}

def roll_dice():
    return random.randint(1, 6)

def get_position(player_name, current_position):
    dice = roll_dice()
    print(f"{player_name} rolled a {dice}.")

    next_position = current_position + dice
    if next_position > FINAL_POSITION:
        print(f"{player_name} cannot move, need exact roll to reach {FINAL_POSITION}.")
        return current_position

    print(f"{player_name} moves from {current_position} to {next_position}")
    if next_position in ladders:
        print(f"Yay! {player_name} climbed a ladder from {next_position} to {ladders[next_position]}")
        next_position = ladders[next_position]

    
    elif next_position in snakes:
        print(f"Oh no! {player_name} got bitten by a snake from {next_position} to {snakes[next_position]}")
        next_position = snakes[next_position]

    return next_position

def play_game():
    print("Welcome to Snake and Ladder Game.")
    print("Version: 1.0.0")
    print("Rules:")
    print("1. All players start at position 0.")
    print("2. Roll the dice and move forward.")
    print("3. Climb ladders. Slide down snakes.")
    print("4. First to reach 100 wins!")
    print("5. Press Enter to roll the dice.")
    print("6. 1-4 players allowed.\n")

    
    while True:
        try:
            num_players = int(input("Enter number of players (1-4): "))
            if 1 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    players = []
    positions = {}

    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        if not name:
            name = f"Player{i + 1}"
        players.append(name)
        positions[name] = 0

    print("\nLet's start the game!\n")

    winner = None
    while not winner:
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            positions[player] = get_position(player, positions[player])
            print(f"{player} is now at position {positions[player]}\n")

            if positions[player] == FINAL_POSITION:
                winner = player
                break

    print(f"Congratulations! {winner} has won the game!")


if __name__ == "__main__":
    play_game()