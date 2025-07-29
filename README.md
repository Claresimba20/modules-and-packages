This is my modules and packages folder
I have divided it into the subfolders operations,test modules and snakes_and_ladders.py

## Snakes_and_ladders.py
## Instructions
Build a Python Script to play Snakes and Ladders versus two players.

## Rules of the game
Initially all the players are at starting position i.e. 0. 
Take it in turns to roll the dice. 
Move forward the number of spaces shown on the dice.
If you land at the bottom of a ladder, you can move up to the top of the ladder.
If you land on the head of a snake, you must slide down to the bottom of the snake.
The first player to get to the FINAL position is the winner.
Hit enter to roll the dice.
Sign up the number of players and names to begin

## An explanation to the code
1.Snakes and ladders mapping
Snakes: If a player lands on one of these keys, they slide down to the corresponding value.
Ladders: If a player lands on one of these keys, they climb up to the corresponding value.

2.def roll_dice():
    return random.randint(1, 6)
Simulates rolling a 6-sided dice.

3.def get_position(player_name, current_position):
This Rolls the dice, Adds the dice roll to the current position, Checks if the new position is on a snake or ladder,If so, it moves the player accordingly.
If the player would go beyond 100, their turn is skipped.

4.def play_game():
This Prompts for number of players (1–4).
Takes each player’s name (or assigns default).
Initializes all players at position 0.
In a loop:
Each player rolls the dice by pressing Enter.
The game prints their movement and new position.
The first to reach 100 wins.

5.if __name__ == "__main__":
    play_game()
This makes sure the game runs only when the script is executed directly




