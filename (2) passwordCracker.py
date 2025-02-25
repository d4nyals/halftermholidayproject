import pygame
import random

# initialise pygame
pygame.init()

# set up screen dimensions
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

# set up the clock to control the frame rate
clock = pygame.time.Clock()

# global variables for storing the current password and user input
current_password = None
user_input = ""


# button class to handle button creation, drawing, and interaction
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        """initialise button with given position, size, text, and optional action"""
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.default_color = WHITE  # default button color
        self.hover_color = GRAY  # color when hovered

    def draw(self, screen):
        """draw the button with text on the screen"""
        mouse_pos = pygame.mouse.get_pos()

        # check if the mouse is hovering over the button
        if self.rect.collidepoint(mouse_pos):  # if mouse is over the button
            button_color = self.hover_color  # change color when hovered
        else:
            button_color = self.default_color  # default button color

        # draw the button with the selected color
        pygame.draw.rect(screen, button_color, self.rect)
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
        current_password = generate_password()  # generate password only once
        print(f"generated password: {current_password}")  # print password for testing in terminal

    while True:
        screen.fill(WHITE)  # fill the screen with a white background
        # draw the buttons (enter, exit, generate)
        enter_button.draw(screen)
        exit_button.draw(screen)
        generate_button.draw(screen)

        # check for events (user interactions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exit the game if user closes the window
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # get the mouse position
                # check if any button is clicked
                enter_button.click(pos)
                exit_button.click(pos)
                generate_button.click(pos)

        pygame.display.update()  # update the screen
        clock.tick(60)  # control the frame rate


def password_input_page():
    global user_input

    while True:
        screen.fill(WHITE)  # fill the screen with white

        # draw "Enter Password" text
        text_surface = font.render("Enter password:", True, BLACK)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 50))

        # draw the input box (for the user to type the password)
        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, 150, 300, 40)  # input box position and size
        pygame.draw.rect(screen, GRAY, input_box)  # fill input box with gray color
        pygame.draw.rect(screen, BLACK, input_box, 2)  # black border around the input box

        # draw the user's typed input inside the box
        input_surface = font.render(user_input, True, BLACK)
        screen.blit(input_surface,
                    (SCREEN_WIDTH // 2 - input_surface.get_width() // 2, 150 + (40 - input_surface.get_height()) // 2))

        # draw submit and exit buttons
        submit_button.draw(screen)
        exit_button.draw(screen)

        # check for events (user interactions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exit the game if user closes the window
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # get mouse position
                # check if any button is clicked
                submit_button.click(pos)
                exit_button.click(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  # remove last character on backspace
                elif event.key == pygame.K_RETURN:
                    check_password()  # check the entered password when enter is pressed
                else:
                    user_input += event.unicode  # add typed character to the input

        pygame.display.update()  # update the screen
        clock.tick(60)  # control the frame rate


def check_password():
    """check if the entered password is correct"""
    global user_input
    if user_input.strip() == current_password:  # compare entered password with correct password
        display_message("access granted!", GREEN)  # display success message
        pygame.quit()  # exit the game after successful login
        quit()
    else:
        display_message("incorrect password", RED)  # display failure message


def display_message(message, color):
    """display a message on the screen"""
    screen.fill(WHITE)  # clear the screen
    text_surface = font.render(message, True, color)  # render the message text
    screen.blit(text_surface, (
    SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2))  # position the message in the center
    pygame.display.update()  # update the screen
    pygame.time.wait(2000)  # wait for 2 seconds to show the message
    password_input_page()  # go back to password input page


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

        # draw the back button
        back_button.draw(screen)

        # check for events (user interactions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exit the game if user closes the window
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # get mouse position
                # check if back button is clicked
                back_button.click(pos)

        pygame.display.update()  # update the screen
        clock.tick(60)  # control the frame rate


def back_to_game_page():
    """back to the main page after generating the password"""
    game_page()


# buttons sizes and shapes
enter_button = Button(75, 300, 225, 50, "Enter password", password_input_page)
exit_button = Button(325, 300, 225, 50, "Go back", exit_app)
submit_button = Button(200, 230, 200, 50, "Submit", check_password)
generate_button = Button(150, 100, 300, 100, "passwordCracka.exe", generate_and_display_password)
back_button = Button(325, 300, 225, 50, "Back to main", back_to_game_page)

# main loop for the password generator page
game_page()

# exit the game
pygame.quit()
