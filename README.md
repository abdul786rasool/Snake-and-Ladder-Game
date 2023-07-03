#Snake-and-Ladder-Game
I have designed snake and ladder playing game for two players using turtle graphics in python.
Snake and Ladder Game:
__________________________________________
The Snake and Ladder Game is a classic board game where players aim to reach the final position on the board by rolling a dice and moving their game piece accordingly. The board consists of numbered squares from 1 to 100. The game includes various attributes associated with certain squares, which add excitement and unpredictability to the gameplay.

The main attributes in the game are:
__________________________________________

1)Ladders (L): Ladders allow players to climb up to a higher-numbered square in a single move. When a player lands on a square with a ladder Ln, they immediately move to the higher-numbered square n, skipping the squares in between.

2)Snakes (S): Snakes are obstacles in the game that bring players down to a lower-numbered square. When a player lands on a square with a snake Sn, they slide down to the lower-numbered square n, bypassing the squares in between.

3)Move Restrictions (R): Move restrictions impose limitations on the possible moves a player can make from a particular square. The attribute Rn denotes that players can make any move except n. It restricts the player from making a specific move, adding a strategic element to the game.

4)Special Moves (M): Special moves allow players to make only a specific move from a square. The attribute Mn indicates that players can only make a move of size n from that square. This adds additional challenges and decision-making to the gameplay.

Game-Play
_____________________
The game is designed for two players and utilizes the turtle graphics library in Python. The game board is drawn on the screen using turtle graphics, creating a visual representation of the playing field.

At the beginning of the game, the players' tokens are placed on the starting square. The players take turns rolling a dice, which determines the number of steps they can move on the board. The dice roll is simulated, and the result is displayed to the players.

Using the turtle graphics, the players' tokens are moved on the board based on the number of steps rolled. The movement is visually represented by the tokens advancing on the board, providing an interactive and engaging experience.

After each player takes their turn, the game checks if any player has reached the final square. If a player lands on a ladder, they are automatically moved to a higher square, giving them an advantage. On the other hand, if a player lands on a snake, they are moved to a lower square, creating a setback for their progress.

The game continues until one of the players reaches the final square. At that point, the game declares the player as the winner and the game concludes.

This implementation of the Snake and Ladder game combines the excitement of rolling dice, strategic movement on the board, and visual feedback through turtle graphics, creating an engaging and enjoyable gaming experience for the players.
