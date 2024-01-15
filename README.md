# Tic-Tac-Toe-Minimax
Playable Tic-Tac-Toe, functionality is a minimax search algorithm to play the best possible move, with option to turn on alpha-beta pruning.

## How to Run
1. Ensure your system has Python installed.
2. Run program using
```
python ttt.py
```

## Commands to Interact
Once the you are running the program, here is a list of commands to interact/play the game.
1. move
- type "move (player) (row) (collumn)"
- ex. move X A 1
- this will make a move on the game board, placing the player on the spot according to the row and collumn
- player can only be 'X' and 'O'
- ensure player and row is CAPITAL letters

2. show
- type "show"
- this will display the current state of the game board

3. reset
- type "reset"
- this will reset the game board to an empty state, allowing to restart the game

4. choose
- type "choose (player)"
- this will call the minimax function to make a move for the given player

5. quit
- type "quit"
- this will end the program

6. pruning
- type "pruning"
- this will run the alpha beta pruning minimax search instead of the normal minimax search
  (i.e. a more efficient version of the minimax search algorithm)

## What I Learned
1. Minimax search algorithm
2. Alpha Beta Pruning
