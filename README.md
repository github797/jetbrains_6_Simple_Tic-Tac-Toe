# Simple Tic-Tac-Toe

Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os.
Tic-tac-toe is played by two players on a 3x3 grid. 

One of the players is 'X', and the other player is 'O'. X plays first, then O takes the next turn, and so on.
The first player that puts 3 X's or 3 O's in a straight line (including diagonals) wins the game.

---
To make it possible for a user to make a move, we need to divide the grid into cells. 
The top left cell has the coordinates (1, 1) and the bottom right cell has the coordinates (3, 3):

    (1, 1) (1, 2) (1, 3)
    (2, 1) (2, 2) (2, 3)
    (3, 1) (3, 2) (3, 3)

The first coordinate goes from top to bottom and the second coordinate goes from left to right. The coordinates can include the numbers 1, 2, or 3.

The program asks the user to enter the coordinates of the cell where they want to make a move.
The user should input 2 coordinate numbers, for example, `1 1`.
If the input is incorrect, the program informs the user why their input is wrong:\
`This cell is occupied! Choose another one!` -  if the cell is not empty.\
`You should enter numbers!` - if the user enters non-numeric symbols in the coordinates input.\
`Coordinates should be from 1 to 3!` - if the user enters coordinates outside the game grid.\
The program keep prompting the user to enter the coordinates until the user input is valid.
If the input is correct, it prints the updated grid to the console including the user's move.

---
The game ends when someone wins or there is a draw. Then the program outputs the final result.
Possible states:\
`Draw` - when no side has a three in a row and the grid has no empty cells.\
`X wins` - when the grid has three X's in a row (including diagonals).\
`O wins` - when the grid has three O's in a row (including diagonals).

---
**Thanks to this app, you can always challenge a friend to play a quick game of Tic-Tac-Toe!**
