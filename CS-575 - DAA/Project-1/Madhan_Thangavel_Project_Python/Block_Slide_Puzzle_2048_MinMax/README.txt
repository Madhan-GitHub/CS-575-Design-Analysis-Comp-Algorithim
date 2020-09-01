Name : Madhan Thangavel
ID : B00814916
CS - 575-20 Project (Block Slide Puzzle (2048) Using Min-max Algorithm)

Programming language used : Python

***********************************************************************************************************************************************************************
Introduction:

Here, an instance of 2048 is played in a 4x4 grid, with numbered tiles that slide in all four directions. 

1.In every turn, a new tile will randomly appear in an empty slot on the board, with a value of either 2 or 4. 
2.The player can slide the tiles in all the four directions (Up, Down, Left and Right). As per the input direction given by the player, 
  all tiles on the grid slide as far as possible in that direction, until (1) they either collide with another tile or (2) collide with the edge of the grid. 
3.If two tiles with the same number collide, then they merge into a single tile with value twice as that of the individual tiles. It has to be noted that 
  the resulting tile will not collide with another tile in the same move. 
4.In this project, the game of 2048 is solved using the Minimax algorithm. Here, 2048 is 
treated as an adversarial game where the player is the computer which is attempting to maximize the value of the highest tile in the grid and the opponent is the 
computer which randomly places tiles in the grid to minimize the maximum score. Minimax algorithm would be suitable in this case as the game is played between 
opponents with a known motive of maximizing/minimizing a total score.(To run "python GameManager.py")
5. Apart from that manual mode is enabled to play the geame individually in the terminal/console.(To run "python Main_Manual.py")

***********************************************************************************************************************************************************************
Code Organization:

GameManager :  Driver program that loads Computer and Player and begins the game where they compete with each other. 
	           Note that the time for making a move is kept as 2 seconds. 

Grid : Defines the Grid object. Incorporates useful operations for the grid like move, getAvailableCells, insertTile and clone

Base : Base class for any  component. All inherit from this module and implement the getMove function which takes a Grid object as parameter and returns a move

Computer : This inherits from Base. The getMove() function returns a computer action, i.e. a tuple (x, y) indicating the place you want to place a tile

Player : Gets the next move for the player using Minmax Algorithm 

Minmax : Implements the Minmax algorithm

Minmaxab : Implements the Minmax algorithm with pruning (Depth limit is set as 4)

Helper : All utility functions created for this game are written here. This includes the eval function which evaluates the heuristic score for a given configuration

Main_Manual : All the configurations of game and its logics are implemented here which enables the user to play using the keys

***********************************************************************************************************************************************************************
Requirements:

Python 3 and above.

Use the below link for import functionalities(if any), Similar commands can be:
	1. https://inventwithpython.com/pygame/chapter1.html
	2. https://stackoverflow.com/questions/18317521/importerror-no-module-named-pygame

Note: Python 2.7.16 (default, Oct 10 2019, 22:02:15) is the version available in remote.cs systems

***********************************************************************************************************************************************************************
How to execute:

Manual mode : python Main_Manual.py

Auto mode : python GameManager.py 

Note : Program Runs utill the game ends.(Game end is where no similar tile is adjacent to each other, and no more tile can be added in the grid)

***********************************************************************************************************************************************************************