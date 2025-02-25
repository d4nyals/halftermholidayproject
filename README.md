# halftermholidayproject
half term holiday project funnn

The code provided is a Python program that uses the pygame library to create a simple graphical password cracker game. Here's a breakdown of what the code is doing:

Initialization:

The pygame library is initialized, and a screen of 600x400 pixels is set up.
Colors (white, green, red, black, gray) and fonts are defined for use in the game.
A clock is set up to control the frame rate of the game.
Global Variables:

current_password: Stores the randomly generated password.
user_input: Stores the user's input as they type the password.
Button Class:

A class called Button is defined to handle button creation, drawing, and clicking.
The Button class has methods to draw the button on the screen and check if it has been clicked.
Password Generation:

generate_password() function generates a random 4-digit password.
Game Page:

game_page() function is the main loop of the game where buttons (enter, exit, generate) are drawn, and user interactions are checked.
If the user clicks the generate button, the password is generated and displayed.
Password Input Page:

password_input_page() function allows the user to enter the password.
The user can type into an input box, and their input is displayed on the screen.
The user can submit the password or exit the game.
Password Checking:

check_password() function compares the user's input with the generated password.
If the password is correct, a success message is displayed; otherwise, a failure message is shown.
Displaying Messages:

display_message() function displays messages on the screen (e.g., "Access granted!" or "Incorrect password").
Exit and Generate Password Functions:

exit_app() function navigates back to the main page.
generate_and_display_password() function displays the generated password on the screen.
back_to_game_page() function navigates back to the main game page.
Buttons Setup:

Buttons for different actions (enter password, exit, submit, generate password, back) are created and assigned their respective actions.
Main Game Loop:

game_page() function is called to start the main loop of the game.
Overall, this program sets up a simple graphical interface for a password cracker game where the user can generate a password, enter it, and check if it matches the generated password. The game uses buttons for navigation and actions, and pygame handles the graphical display and user interactions.
