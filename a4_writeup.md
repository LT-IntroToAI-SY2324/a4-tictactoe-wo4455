# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
The most difficult part of this tic-tac-toe assignment was to create a solution that returns true if a player has won the game. You need to take into account all possibilities that could occur. 

2. Explain how you would add a computer player to the game.
I would add a computer player to this game by looking at where the human player moves, and analyze where the next best move would be based on that move. I would have the computer place a move in that spot, and then give the human player another move, and so on. 

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
I could look at where the human player makes a certain move on the board (the index of self.board) and look at all spaces around that space that could be the same player (like if the player is O, check if there is an O above, below, and to all sides of where the player put the move). If there is a pattern where it would lead to having 3 in a row, the computer can make a move accordingly based on the situation. This solution includes a lot of trial and error when looking for every possibility that could occur and find the best move based on the information that it gets. 