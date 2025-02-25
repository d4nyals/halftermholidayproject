import pygame
import random

# initialise pygame
pygame.init()

# set up the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("passwordCracker.exe")

# define colours using RGB values
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)

# define fonts for rendering text on the screen
font = pygame.font.SysFont("Comic Sans MS", 30)
small_font = pygame.font.SysFont("Comic Sans MS", 20)

# sets the clock for controlling the frame rate
clock = pygame.time.Clock()

# global variables for storing password and user input
current_password = None
user_input = ""

# button class to handle button creation, drawing, and clicking
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        """initialise button with given position, size, text, and optional action"""
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, screen):
        """draw the button with text on the screen"""
        # draw white button with black border
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)  # black outline
        text_surface = font.render(self.text, True, BLACK)
        # position the text in the center of the button
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) / 2,
                                  self.rect.y + (self.rect.height - text_surface.get_height()) / 2))

    def click(self, pos):
        """check if the button is clicked and execute its action"""
        if self.rect.collidepoint(pos):
            if self.action:
                self.action()


def generate_password():
    """generate a random 4-digit password"""
    return str(random.randint(1000, 9999))


def game_page():
    global current_password
    if current_password is None:
        current_password = generate_password()  # generate the password only once
        print(f"generated password: {current_password}")  # print password for testing in terminal

    while True:
        screen.fill(WHITE)  # fillss the screen with a white background
        # draw the buttons (enter, exit, generate)
        enter_button.draw(screen)
        exit_button.draw(screen)
        generate_button.draw(screen)

        # check for events (user interactions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exits the game if the user closes the window
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # gets the mouse position
                # check if any button is clicked
                enter_button.click(pos)
                exit_button.click(pos)
                generate_button.click(pos)

        pygame.display.update()  # update the screen
        clock.tick(60)  # controls the frame rate (60 fps)


def password_input_page():
    global user_input

    while True:
        screen.fill(WHITE)  # fills the screen with a white background

        # draws the "Enter Password" text
        text_surface = font.render("Enter password:", True, BLACK)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 50))

        # draw the input box (for the user to type the password)
        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, 150, 300, 40)  # position and size of the input box
        pygame.draw.rect(screen, GRAY, input_box)  # fill the input box with a grey colour
        pygame.draw.rect(screen, BLACK, input_box, 2)  # black border around the input box

        # draw the user's typed input inside the box
        input_surface = font.render(user_input, True, BLACK)
        screen.blit(input_surface, (SCREEN_WIDTH // 2 - input_surface.get_width() // 2, 150 + (40 - input_surface.get_height()) // 2))

        # draw the submit and exit buttons
        submit_button.draw(screen)
        exit_button.draw(screen)

        # check for events (user interactions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exit the game if the user closes the window
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # get the mouse position
                # check if any button is clicked
                submit_button.click(pos)
                exit_button.click(pos)
            elif event.type == pygame.KEYDOWN:
                # if the user presses backspace, remove the last character
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                # if the user presses return, check the entered password
                elif event.key == pygame.K_RETURN:
                    check_password()
                else:
                    # append the entered character to the input string
                    user_input += event.unicode

        pygame.display.update()  # update the screen
        clock.tick(60)  # control the frame rate


def check_password():
    """check if the entered password is correct"""
    global user_input
    if user_input.strip() == current_password:  # compare entered password with the correct one
        display_message("Access granted!", GREEN, True)  # display success message and exit
    else:
        display_message("Incorrect password", RED, False)  # display failure message


def display_message(message, color, exit_game=False):
    """display a message on the screen"""
    screen.fill(WHITE)  # clear the screen
    text_surface = font.render(message, True, color)  # render the message text
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2))  # position the message in the centre
    pygame.display.update()  # update the screen
    pygame.time.wait(2000)  # wait for 2 seconds to show the message

    if exit_game:  # if access granted, exit the game
        pygame.quit()
        quit()
    else:
        password_input_page()  # go back to the password input page


def exit_app():
    """navigate back to the main page, not quit the program"""
    game_page()


def generate_and_display_password():
    global current_password  # use the global variable for password

    if current_password is None:  # only generate if it's not already set
        current_password = generate_password()

    while True:
        screen.fill(WHITE)  # fill the screen with a white background
        # display the generated password
        password_message = f"The password is: {current_password}"
        text_surface = font.render(password_message, True, BLACK)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 3))


        # draw the "back" button
        back_button.draw(screen)

        # check for events (user interactions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exit the game if the user closes the window
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # get the mouse position
                # check if the back button is clicked
                back_button.click(pos)

        pygame.display.update()  # update the screen
        clock.tick(60)  # control the frame rate


def back_to_game_page():
    """back to the main page after generating the password"""
    game_page()


# buttons sizes and shapes and whatever
enter_button = Button(75, 300, 225, 50, "Enter password", password_input_page)
exit_button = Button(325, 300, 225, 50, "Go back", exit_app)
submit_button = Button(200, 230, 200, 50, "Submit", check_password)
generate_button = Button(150, 100, 300, 100, "passwordCracka.exe", generate_and_display_password)
back_button = Button(325, 300, 225, 50, "Back to main", back_to_game_page)

# main loop for password generator page?
game_page()

# exiting the game
pygame.quit()
