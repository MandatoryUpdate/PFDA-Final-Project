# PROJECT TITLE
Jumpy Jump
## Demo
Demo Video: https://youtu.be/YU60c7QBBI4

## GitHub Repository
GitHub Repo: https://github.com/MandatoryUpdate/PFDA-Final-Project.git

## Description
This project was a simple exercise in implementing Python code to make a functioning game akin to Doodle Jump. There aren't many files inside the game, just the project.py, which contains all
the source code in this project. There are several mechancis involved with this game. The first is a movement mechanic that allows the player to move left and right as they move up on the screen. Similarly,
there is a jump mechanic that is outside of the player's control, to allow for the game to be more fast paced and entertaining. There also exists 2 different states for the game to be in, the game menu and the
game over screen. The game over screen exists as a transition between going back to the menu (Though there is not really a point to do so at the moment) or restarting. The game menu simply allows for you to
start the game. Frankly, they don't add much, but I felt that this game required another feature in order to properly be considered a game.


There a few improvements that need to be done in order to polish this game further. The first would be a way to keep permanent track of the best score achieved. As it is now, the game only tracks
the relative best score. There's also an issue with how the player interacts with the bottom of the screen. Occasionally, the player will bounce at the death boundary, rather than properly dying.
Most likely the issue is with how the character is interacting with that border, as well as lingering hitboxes. That will require some severe bug fixing which may not be doable at my current skill level.
Another important thing to add would have to be better graphics. The game only functions on simple shapes rather than actual images, which diminishes the idea that this is a game. I'd also like to 
change the movement system so that a player is not infinintely moving in a direction after a movement key is pressed. I couldn't fix that issue in time, and it wasn't that big of a problem, so I left it
as is.

## Tutorials Used
# For scene switching:
https://stackoverflow.com/questions/63317696/a-good-way-to-switch-to-a-menu-using-pygame

# For button mechanics and platform mechanics:
https://www.youtube.com/watch?v=BHr9jxKithk
